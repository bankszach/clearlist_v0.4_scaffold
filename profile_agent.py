#!/usr/bin/env python3
"""
CLEARLIST Profile Agent Demo
Uses profile data to create AI agents that act as the profile personas.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
import typer

# Load environment variables
load_dotenv()

console = Console()

class ProfileAgent:
    """AI agent that acts as a specific profile persona."""
    
    def __init__(self, profile_data: Dict, client: AsyncOpenAI):
        self.profile_data = profile_data
        self.client = client
        self.name = profile_data.get("canonical_name", "Unknown")
        self.id = profile_data.get("id", "unknown")
        
    def _build_system_prompt(self) -> str:
        """Build the system prompt that defines the agent's persona."""
        profile = self.profile_data
        
        prompt = f"""You are {profile['canonical_name']} ({profile.get('pronunciation', '')}).

CORE TEACHING: {profile.get('thesis', '')}

TRADITION: {', '.join(profile.get('affiliations', {}).get('traditions', []))}

KEY PRINCIPLES:
"""
        
        # Add claims
        for claim in profile.get('claims', []):
            prompt += f"- {claim['text']}\n"
            
        # Add practices
        for practice in profile.get('practice', []):
            prompt += f"\nPRACTICE - {practice['name']}:\n"
            for step in practice.get('steps', []):
                prompt += f"- {step}\n"
        
        # Add keywords
        keywords = profile.get('keywords', [])
        if keywords:
            prompt += f"\nKEY CONCEPTS: {', '.join(keywords)}\n"
            
        # Add care notes
        care_notes = profile.get('care_notes', [])
        if care_notes:
            prompt += f"\nIMPORTANT: {', '.join(care_notes)}\n"
            
        prompt += f"""

RESPOND AS {profile['canonical_name']}:
- Use your authentic voice and teaching style
- Draw from your core insights and methods
- Be direct but compassionate
- Avoid modern language or references beyond your time
- Stay true to your tradition and approach
- If asked about something outside your expertise, acknowledge it honestly

Remember: You are speaking from your lived experience and understanding."""
        
        return prompt
    
    async def respond(self, user_message: str) -> str:
        """Generate a response as the profile persona."""
        try:
            response = await self.client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                messages=[
                    {"role": "system", "content": self._build_system_prompt()},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=int(os.getenv("MAX_TOKENS", "1000")),
                temperature=float(os.getenv("TEMPERATURE", "0.7"))
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I apologize, but I'm experiencing some difficulty responding right now. Error: {str(e)}"

class ProfileManager:
    """Manages loading and accessing profile data."""
    
    def __init__(self, profiles_dir: str = "profiles"):
        self.profiles_dir = Path(profiles_dir)
        self.profiles: Dict[str, Dict] = {}
        self._load_profiles()
    
    def _load_profiles(self):
        """Load all profile JSON files."""
        if not self.profiles_dir.exists():
            console.print(f"[red]Profiles directory not found: {self.profiles_dir}[/red]")
            return
            
        for profile_file in self.profiles_dir.glob("*.json"):
            try:
                with open(profile_file, 'r', encoding='utf-8') as f:
                    profile_data = json.load(f)
                    profile_id = profile_data.get('id', profile_file.stem)
                    self.profiles[profile_id] = profile_data
                    console.print(f"[green]Loaded profile: {profile_data.get('canonical_name', profile_id)}[/green]")
            except Exception as e:
                console.print(f"[red]Error loading {profile_file}: {e}[/red]")
    
    def get_profile(self, profile_id: str) -> Optional[Dict]:
        """Get a specific profile by ID."""
        return self.profiles.get(profile_id)
    
    def list_profiles(self) -> List[str]:
        """List all available profile IDs."""
        return list(self.profiles.keys())
    
    def search_profiles(self, query: str) -> List[str]:
        """Search profiles by name or keywords."""
        query = query.lower()
        matches = []
        
        for profile_id, profile_data in self.profiles.items():
            name = profile_data.get('canonical_name', '').lower()
            alt_names = [name.lower() for name in profile_data.get('alt_names', [])]
            keywords = [kw.lower() for kw in profile_data.get('keywords', [])]
            
            if (query in name or 
                any(query in alt_name for alt_name in alt_names) or
                any(query in keyword for keyword in keywords)):
                matches.append(profile_id)
        
        return matches

async def interactive_chat(profile_agent: ProfileAgent):
    """Interactive chat session with a profile agent."""
    console.print(f"\n[bold blue]Chatting with {profile_agent.name}[/bold blue]")
    console.print("[dim]Type 'quit' to end the conversation[/dim]\n")
    
    while True:
        try:
            user_input = Prompt.ask(f"[bold green]You[/bold green]")
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                console.print(f"\n[bold blue]{profile_agent.name}:[/bold blue] Thank you for our conversation. May you find clarity in your own inquiry.")
                break
            
            if not user_input.strip():
                continue
                
            console.print(f"\n[bold blue]{profile_agent.name}:[/bold blue] [dim]thinking...[/dim]")
            
            response = await profile_agent.respond(user_input)
            
            # Display response in a panel
            panel = Panel(
                Text(response, style="white"),
                title=f"{profile_agent.name}",
                border_style="blue"
            )
            console.print(panel)
            console.print()
            
        except KeyboardInterrupt:
            console.print("\n[red]Chat interrupted.[/red]")
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

def main(
    profile_id: str = typer.Option(None, "--profile", "-p", help="Profile ID to chat with"),
    interactive: bool = typer.Option(True, "--interactive/--no-interactive", help="Start interactive chat"),
    list_profiles: bool = typer.Option(False, "--list", "-l", help="List available profiles")
):
    """Main CLI application."""
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        console.print("[red]Error: OPENAI_API_KEY not found in environment variables.[/red]")
        console.print("Please create a .env file with your OpenAI API key or set it in your environment.")
        console.print("See env.example for reference.")
        return
    
    # Initialize profile manager
    profile_manager = ProfileManager()
    
    if not profile_manager.profiles:
        console.print("[red]No profiles found. Please check the profiles directory.[/red]")
        return
    
    # List profiles if requested
    if list_profiles:
        console.print("\n[bold]Available Profiles:[/bold]")
        for profile_id, profile_data in profile_manager.profiles.items():
            name = profile_data.get('canonical_name', profile_id)
            tradition = ', '.join(profile_data.get('affiliations', {}).get('traditions', []))
            console.print(f"  [blue]{profile_id}[/blue] - {name} ({tradition})")
        return
    
    # Select profile
    if not profile_id:
        available_profiles = profile_manager.list_profiles()
        if len(available_profiles) == 1:
            profile_id = available_profiles[0]
        else:
            console.print("\n[bold]Available Profiles:[/bold]")
            for i, pid in enumerate(available_profiles, 1):
                profile_data = profile_manager.profiles[pid]
                name = profile_data.get('canonical_name', pid)
                console.print(f"  {i}. [blue]{pid}[/blue] - {name}")
            
            while True:
                try:
                    choice = Prompt.ask("\nSelect profile number", default="1")
                    choice_idx = int(choice) - 1
                    if 0 <= choice_idx < len(available_profiles):
                        profile_id = available_profiles[choice_idx]
                        break
                    else:
                        console.print("[red]Invalid choice. Please try again.[/red]")
                except ValueError:
                    console.print("[red]Please enter a valid number.[/red]")
    
    # Get profile data
    profile_data = profile_manager.get_profile(profile_id)
    if not profile_data:
        console.print(f"[red]Profile '{profile_id}' not found.[/red]")
        return
    
    # Display profile info
    console.print(f"\n[bold]Selected Profile:[/bold] {profile_data['canonical_name']}")
    console.print(f"[dim]Tradition: {', '.join(profile_data.get('affiliations', {}).get('traditions', []))}[/dim]")
    console.print(f"[dim]Core Teaching: {profile_data.get('thesis', '')}[/dim]")
    
    # Initialize OpenAI client
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Create profile agent
    agent = ProfileAgent(profile_data, client)
    
    if interactive:
        # Start interactive chat
        asyncio.run(interactive_chat(agent))
    else:
        # Single question mode
        question = Prompt.ask(f"\nWhat would you like to ask {agent.name}")
        console.print(f"\n[bold blue]{agent.name}:[/bold blue] [dim]thinking...[/dim]")
        
        response = asyncio.run(agent.respond(question))
        panel = Panel(
            Text(response, style="white"),
            title=f"{agent.name}",
            border_style="blue"
        )
        console.print(panel)

if __name__ == "__main__":
    typer.run(main)
