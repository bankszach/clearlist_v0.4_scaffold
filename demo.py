#!/usr/bin/env python3
"""
Simple demo script for the CLEARLIST Profile Agent system.
This shows how to use the system programmatically.
"""

import asyncio
import os
from dotenv import load_dotenv
from profile_agent import ProfileManager, ProfileAgent
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

async def demo_conversation():
    """Demonstrate a conversation with a profile agent."""
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found. Please set it in your .env file.")
        return
    
    # Initialize components
    profile_manager = ProfileManager()
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Get a profile (let's use Ramana Maharshi as an example)
    profile_data = profile_manager.get_profile("ramana-maharshi")
    if not profile_data:
        print("Profile not found!")
        return
    
    # Create the agent
    agent = ProfileAgent(profile_data, client)
    
    print(f"Demo: Chatting with {agent.name}")
    print("=" * 50)
    
    # Sample questions to demonstrate the system
    questions = [
        "What is your core teaching method?",
        "How should I practice self-inquiry?",
        "What is the nature of the Self?",
        "How do you approach silence and meditation?"
    ]
    
    for question in questions:
        print(f"\nQ: {question}")
        print("-" * 30)
        
        response = await agent.respond(question)
        print(f"A: {response}")
        print()
        
        # Small delay to avoid rate limiting
        await asyncio.sleep(1)

def demo_profile_loading():
    """Demonstrate profile loading and management."""
    print("Profile Loading Demo")
    print("=" * 30)
    
    profile_manager = ProfileManager()
    
    print(f"Loaded {len(profile_manager.profiles)} profiles:")
    for profile_id, profile_data in profile_manager.profiles.items():
        name = profile_data.get('canonical_name', profile_id)
        tradition = ', '.join(profile_data.get('affiliations', {}).get('traditions', []))
        thesis = profile_data.get('thesis', 'No thesis available')
        print(f"\n{name} ({profile_id})")
        print(f"  Tradition: {tradition}")
        print(f"  Core Teaching: {thesis[:100]}...")

if __name__ == "__main__":
    print("CLEARLIST Profile Agent Demo")
    print("=" * 40)
    
    # Demo profile loading
    demo_profile_loading()
    
    print("\n" + "=" * 40)
    
    # Demo conversation (requires API key)
    if os.getenv("OPENAI_API_KEY"):
        print("\nStarting conversation demo...")
        asyncio.run(demo_conversation())
    else:
        print("\nSkipping conversation demo - no API key found.")
        print("Set OPENAI_API_KEY in your .env file to test the AI conversation.")
