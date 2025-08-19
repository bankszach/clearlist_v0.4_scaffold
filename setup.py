#!/usr/bin/env python3
"""
Setup script for the CLEARLIST Profile Agent Demo system.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required, found {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required Python packages."""
    print("\n📦 Installing dependencies...")
    
    # Check if pip is available
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ pip not available. Please install pip first.")
        return False
    
    # Install requirements
    if os.path.exists("requirements.txt"):
        success = run_command(
            f"{sys.executable} -m pip install -r requirements.txt",
            "Installing packages from requirements.txt"
        )
        if not success:
            return False
    else:
        print("⚠️  requirements.txt not found, installing core packages...")
        packages = ["openai", "python-dotenv", "rich", "typer", "pydantic"]
        for package in packages:
            success = run_command(
                f"{sys.executable} -m pip install {package}",
                f"Installing {package}"
            )
            if not success:
                return False
    
    return True

def setup_environment():
    """Set up environment configuration."""
    print("\n🔧 Setting up environment...")
    
    env_file = Path(".env")
    env_example = Path("env.example")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_example.exists():
        print("📋 Creating .env file from template...")
        try:
            with open(env_example, 'r') as src, open(env_file, 'w') as dst:
                content = src.read()
                dst.write(content)
            print("✅ .env file created from template")
            print("⚠️  Please edit .env and add your OpenAI API key")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    else:
        print("⚠️  No env.example found, creating basic .env...")
        try:
            with open(env_file, 'w') as f:
                f.write("# OpenAI API Configuration\n")
                f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
                f.write("OPENAI_MODEL=gpt-4o-mini\n")
                f.write("MAX_TOKENS=1000\n")
                f.write("TEMPERATURE=0.7\n")
            print("✅ Basic .env file created")
            print("⚠️  Please edit .env and add your OpenAI API key")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False

def test_installation():
    """Test that the installation works."""
    print("\n🧪 Testing installation...")
    
    try:
        # Test importing main modules
        import profile_agent
        print("✅ profile_agent module imported successfully")
        
        # Test profile loading
        profile_manager = profile_agent.ProfileManager()
        if profile_manager.profiles:
            print(f"✅ Profile loading works: {len(profile_manager.profiles)} profiles found")
        else:
            print("⚠️  No profiles loaded (check profiles/ directory)")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def main():
    """Main setup function."""
    print("🚀 CLEARLIST Profile Agent Demo Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Setup failed: Python version incompatible")
        return False
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Dependency installation failed")
        return False
    
    # Setup environment
    if not setup_environment():
        print("\n❌ Setup failed: Environment setup failed")
        return False
    
    # Test installation
    if not test_installation():
        print("\n❌ Setup failed: Installation test failed")
        return False
    
    print("\n" + "=" * 40)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env and add your OpenAI API key")
    print("2. Run: python test_system.py")
    print("3. Run: python profile_agent.py --list")
    print("4. Start chatting: python profile_agent.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
