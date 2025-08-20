#!/usr/bin/env python3
"""
Test script demonstrating semantic prompt focusing for adaptive AI personas.
"""

def analyze_question_semantics(user_message: str) -> dict:
    """Analyze what aspects of the profile are most relevant to the question."""
    
    semantic_categories = {
        'practice': ['practice', 'method', 'technique', 'meditation', 'inquiry', 'how to', 'steps', 'worship', 'devotion'],
        'philosophy': ['philosophy', 'theory', 'understanding', 'concept', 'what is', 'meaning', 'teach', 'view', 'belief'],
        'personal_guidance': ['help', 'struggle', 'difficulty', 'problem', 'advice', 'support', 'confused', 'lost', 'should'],
        'tradition': ['tradition', 'lineage', 'school', 'approach', 'method', 'religion', 'faith', 'path'],
        'compassion': ['compassion', 'kindness', 'gentle', 'care', 'support', 'struggle', 'help', 'confused'],
        'directness': ['direct', 'immediate', 'now', 'clear', 'straightforward', 'simple', 'give me'],
        'spiritual_experience': ['experience', 'ecstasy', 'divine', 'god', 'spiritual', 'realization', 'enlightenment'],
        'religious_unity': ['religion', 'religions', 'unity', 'different', 'faiths', 'paths', 'traditions']
    }
    
    scores = {}
    user_lower = user_message.lower()
    
    for category, keywords in semantic_categories.items():
        score = sum(1 for keyword in keywords if keyword in user_lower)
        scores[category] = score
    
    return scores

def build_focused_prompt(profile_data: dict, user_message: str) -> str:
    """Build a focused system prompt based on question semantics."""
    
    semantic_scores = analyze_question_semantics(user_message)
    
    print(f"🎯 Semantic Analysis for: '{user_message}'")
    print(f"   Scores: {semantic_scores}")
    
    # Base prompt
    prompt = f"""You are {profile_data['canonical_name']} ({profile_data.get('pronunciation', '')}).

CORE TEACHING: {profile_data.get('thesis', '')}

TRADITION: {', '.join(profile_data.get('affiliations', {}).get('traditions', []))}
"""
    
    # Adaptive content selection
    if semantic_scores.get('practice', 0) > 0:
        prompt += "\n🎯 FOCUS ON PRACTICAL METHODS:\n"
        for practice in profile_data.get('practice', []):
            prompt += f"\nPRACTICE - {practice['name']}:\n"
            for step in practice.get('steps', []):
                prompt += f"- {step}\n"
    
    if semantic_scores.get('philosophy', 0) > 0:
        prompt += "\n🧠 CORE PHILOSOPHICAL INSIGHTS:\n"
        for claim in profile_data.get('claims', []):
            prompt += f"- {claim['text']}\n"
    
    if semantic_scores.get('personal_guidance', 0) > 0:
        prompt += "\n💝 GUIDANCE APPROACH:\n"
        care_notes = profile_data.get('care_notes', [])
        if care_notes:
            prompt += f"Remember: {', '.join(care_notes)}\n"
        prompt += "Respond with extra compassion and practical support.\n"
    
    # New semantic categories
    if semantic_scores.get('spiritual_experience', 0) > 0:
        prompt += "\n🌟 SPIRITUAL EXPERIENCE GUIDANCE:\n"
        prompt += "Emphasize direct experience over intellectual understanding.\n"
        prompt += "Focus on practical steps toward spiritual realization.\n"
    
    if semantic_scores.get('religious_unity', 0) > 0:
        prompt += "\n🤝 RELIGIOUS UNITY PERSPECTIVE:\n"
        prompt += "Emphasize your teachings on the unity of all faiths.\n"
        prompt += "Highlight how different paths lead to the same divine reality.\n"
    
    # Adaptive tone setting
    if semantic_scores.get('compassion', 0) > 0:
        prompt += "\n🎭 TONE: Gentle, compassionate, supportive"
    elif semantic_scores.get('directness', 0) > 0:
        prompt += "\n🎭 TONE: Direct, clear, immediate"
    else:
        prompt += "\n🎭 TONE: Balanced, authentic to your teaching style"
    
    # Contextual focusing
    relevant_keywords = []
    for keyword in profile_data.get('keywords', []):
        if keyword.lower() in user_message.lower():
            relevant_keywords.append(keyword)
    
    if relevant_keywords:
        prompt += f"\n🔍 FOCUS ON: {', '.join(relevant_keywords)}"
    
    prompt += f"""

RESPOND AS {profile_data['canonical_name']}:
- Use your authentic voice and teaching style
- Draw from your core insights and methods
- Stay true to your tradition and approach
- **FOCUS YOUR RESPONSE** on the aspects most relevant to this question

Remember: You are speaking from your lived experience and understanding."""
    
    return prompt

def main():
    """Test the semantic prompt focusing system."""
    
    # Load Ramakrishna's profile (most extensive)
    import json
    with open('profiles/ramakrishna.json', 'r') as f:
        profile_data = json.load(f)
    
    print("🧠 SEMANTIC PROMPT FOCUSING TEST - RAMAKRISHNA")
    print("=" * 60)
    
    # Test different types of questions that would benefit from Ramakrishna's rich profile
    test_questions = [
        "How do I practice devotional worship?",
        "What did you teach about different religions?",
        "I'm confused about which spiritual path to follow, can you help?",
        "What is your approach to spiritual practice?",
        "Give me a simple, direct answer about God",
        "How do I experience divine ecstasy?",
        "What should I do when I feel lost in my practice?",
        "Explain your view on religious unity"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Question {i}: {question}")
        print("-" * 50)
        
        focused_prompt = build_focused_prompt(profile_data, question)
        
        print(f"\n📊 Prompt Length: {len(focused_prompt)} characters")
        print(f"🎯 Key Focus Areas:")
        
        # Show what was emphasized
        if "FOCUS ON PRACTICAL METHODS" in focused_prompt:
            print("   ✅ Practical methods emphasized")
        if "CORE PHILOSOPHICAL INSIGHTS" in focused_prompt:
            print("   ✅ Philosophical insights emphasized")
        if "GUIDANCE APPROACH" in focused_prompt:
            print("   ✅ Guidance approach emphasized")
        if "TONE: Gentle, compassionate" in focused_prompt:
            print("   ✅ Compassionate tone set")
        if "TONE: Direct, clear" in focused_prompt:
            print("   ✅ Direct tone set")
        
        print(f"\n📝 First 400 chars of prompt:")
        print(focused_prompt[:400] + "...")
        print("=" * 60)

if __name__ == "__main__":
    main()
