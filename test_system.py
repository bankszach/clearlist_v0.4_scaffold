#!/usr/bin/env python3
"""
Test script for the CLEARLIST Profile Agent system.
This tests the basic functionality without requiring an OpenAI API key.
"""

import json
from pathlib import Path
from profile_agent import ProfileManager

def test_profile_loading():
    """Test that profiles can be loaded correctly."""
    print("Testing Profile Loading...")
    
    profile_manager = ProfileManager()
    
    if not profile_manager.profiles:
        print("❌ No profiles loaded!")
        return False
    
    print(f"✅ Loaded {len(profile_manager.profiles)} profiles")
    
    # Check specific profiles
    expected_profiles = ['ramana-maharshi', 'nisargadatta-maharaj', 'anandamayi-ma']
    for profile_id in expected_profiles:
        if profile_id in profile_manager.profiles:
            print(f"✅ Found profile: {profile_id}")
        else:
            print(f"❌ Missing profile: {profile_id}")
            return False
    
    return True

def test_profile_data_structure():
    """Test that profile data has the expected structure."""
    print("\nTesting Profile Data Structure...")
    
    profile_manager = ProfileManager()
    
    for profile_id, profile_data in profile_manager.profiles.items():
        print(f"\nChecking {profile_id}...")
        
        # Check required fields
        required_fields = ['canonical_name', 'thesis', 'affiliations', 'keywords']
        for field in required_fields:
            if field in profile_data:
                print(f"  ✅ {field}: {profile_data[field]}")
            else:
                print(f"  ❌ Missing required field: {field}")
                return False
        
        # Check affiliations structure
        affiliations = profile_data.get('affiliations', {})
        if 'traditions' in affiliations and affiliations['traditions']:
            print(f"  ✅ traditions: {affiliations['traditions']}")
        else:
            print(f"  ⚠️  No traditions specified")
        
        # Check practices
        practices = profile_data.get('practice', [])
        if practices:
            print(f"  ✅ practices: {len(practices)} found")
            for practice in practices:
                if 'name' in practice and 'steps' in practice:
                    print(f"    - {practice['name']}: {len(practice['steps'])} steps")
        else:
            print(f"  ⚠️  No practices specified")
    
    return True

def test_profile_search():
    """Test profile search functionality."""
    print("\nTesting Profile Search...")
    
    profile_manager = ProfileManager()
    
    # Test search by name
    results = profile_manager.search_profiles("ramana")
    if 'ramana-maharshi' in results:
        print("✅ Search by name works")
    else:
        print("❌ Search by name failed")
        return False
    
    # Test search by keyword
    results = profile_manager.search_profiles("nonduality")
    if len(results) > 0:
        print(f"✅ Search by keyword works: {results}")
    else:
        print("❌ Search by keyword failed")
        return False
    
    return True

def test_system_prompt_generation():
    """Test that system prompts can be generated (without API calls)."""
    print("\nTesting Semantic Prompt Generation...")
    
    try:
        from profile_agent import ProfileAgent
        from openai import AsyncOpenAI
        
        # Create a mock client
        mock_client = AsyncOpenAI(api_key="mock_key")
        
        profile_manager = ProfileManager()
        profile_data = profile_manager.get_profile("ramana-maharshi")
        
        if profile_data:
            agent = ProfileAgent(profile_data, mock_client)
            
            # Test different types of questions
            test_questions = [
                "How do I practice self-inquiry?",
                "What is nonduality?",
                "I'm struggling with meditation, help me"
            ]
            
            all_prompts_work = True
            
            for question in test_questions:
                prompt = agent._build_focused_system_prompt(question)
                
                if "Ramana Maharshi" not in prompt:
                    print(f"❌ Missing name in prompt for: {question}")
                    all_prompts_work = False
                    continue
                
                # Check semantic focusing is working
                if "practice" in question.lower() and "FOCUS ON PRACTICAL METHODS" not in prompt:
                    print(f"⚠️  Practice question didn't trigger practice focus: {question}")
                
                if "struggle" in question.lower() and "GUIDANCE APPROACH" not in prompt:
                    print(f"⚠️  Struggle question didn't trigger guidance: {question}")
                
                print(f"✅ Generated {len(prompt)} char prompt for: {question}")
            
            if all_prompts_work:
                print("✅ Semantic prompt generation works")
                return True
            else:
                print("❌ Some semantic prompts failed")
                return False
        else:
            print("❌ Could not get profile data for testing")
            return False
            
    except Exception as e:
        print(f"❌ Error testing semantic prompt generation: {e}")
        return False

def main():
    """Run all tests."""
    print("CLEARLIST Profile Agent System Tests")
    print("=" * 40)
    
    tests = [
        test_profile_loading,
        test_profile_data_structure,
        test_profile_search,
        test_system_prompt_generation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print(f"❌ Test failed: {test.__name__}")
        except Exception as e:
            print(f"❌ Test error in {test.__name__}: {e}")
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
        print("\nTo test with AI conversations, set your OPENAI_API_KEY in .env")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    main()
