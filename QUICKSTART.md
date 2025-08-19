# Quick Start Guide

Get the CLEARLIST Profile Agent Demo running in 5 minutes!

## 🚀 Quick Setup

### 1. Run the Setup Script
```bash
python setup.py
```

This will:
- Check Python version compatibility
- Install all required dependencies
- Create a `.env` file template
- Test the installation

### 2. Add Your OpenAI API Key
Edit the `.env` file and replace `your_openai_api_key_here` with your actual API key:
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

### 3. Test the System
```bash
python test_system.py
```

### 4. Start Chatting!
```bash
# Interactive chat with profile selection
python profile_agent.py

# Or chat with a specific profile
python profile_agent.py --profile ramana-maharshi
```

## 🎯 What You'll Get

- **3 Profile Agents**: Ramana Maharshi, Nisargadatta Maharaj, and Anandamayi Ma
- **Authentic Personas**: Each agent responds in the voice and style of their respective teacher
- **Rich Context**: Responses draw from their actual teachings, practices, and claims
- **Beautiful Interface**: Rich terminal formatting with panels and colors

## 🔍 Available Commands

```bash
# List all available profiles
python profile_agent.py --list

# Chat with a specific profile
python profile_agent.py --profile nisargadatta-maharaj

# Single question mode (non-interactive)
python profile_agent.py --no-interactive --profile anandamayi-ma

# Run the demo script
python demo.py
```

## 🆘 Need Help?

- **Full Documentation**: See `README_demo.md`
- **System Issues**: Run `python test_system.py` to diagnose problems
- **API Issues**: Check your `.env` file and API key

## 🎉 You're Ready!

The system will automatically load all profiles from your `profiles/` directory. Each agent will respond as if they are the actual spiritual teacher, drawing from their documented teachings and methods.

Happy exploring! 🙏
