# CLEARLIST AI Wisdom Agents

**Transform structured spiritual wisdom into interactive AI experiences.**

This system brings the CLEARLIST profiles to life as AI agents that embody each teacher's authentic voice and wisdom. By loading profile JSON files and using them as rich context for OpenAI API calls, each agent responds in the distinctive style and approach of their respective spiritual tradition.

## Features

- **🎭 Authentic Personas**: AI agents that embody each teacher's unique voice, methods, and insights
- **📚 Rich Context**: Comprehensive use of profile data including teachings, practices, claims, and traditions
- **💬 Interactive Wisdom**: Full conversation mode for deep exploration of spiritual concepts
- **🔍 Cross-Tradition Exploration**: Compare approaches across Advaita, Vedānta, and Bhakti traditions
- **⚡ Ready to Use**: Complete Python system with OpenAI integration and beautiful CLI interface
- **🌱 Extensible**: Easy to add new profiles and customize agent behavior

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the environment template and add your OpenAI API key:

```bash
cp env.example .env
```

Edit `.env` and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

### 3. Verify Profile Data

Ensure your `profiles/` directory contains the profile JSON files. The system will automatically load:
- `ramana-maharshi.json`
- `nisargadatta-maharaj.json` 
- `anandamayi-ma.json`

## Usage

### Interactive Chat Mode

Start an interactive chat with a profile agent:

```bash
# Chat with a specific profile
python profile_agent.py --profile ramana-maharshi

# Or let the system prompt you to choose
python profile_agent.py
```

### List Available Profiles

```bash
python profile_agent.py --list
```

### Single Question Mode

```bash
python profile_agent.py --no-interactive --profile nisargadatta-maharaj
```

### Demo Script

Run the included demo script to see the system in action:

```bash
python demo.py
```

## 🌟 Project Significance

This system represents a breakthrough in how structured spiritual data can be used to create meaningful AI experiences. By combining:

- **Structured Wisdom**: CLEARLIST's carefully curated profiles of spiritual teachers
- **AI Technology**: OpenAI's language models for natural conversation
- **Authentic Context**: Rich metadata including teachings, practices, and traditions
- **Semantic Intelligence**: Adaptive prompt focusing that responds to question context

We've created something unique: AI agents that don't just simulate spiritual teachers, but truly embody their documented wisdom and approach with **contextual intelligence**.

## How It Works

### 1. Profile Loading
The `ProfileManager` class scans the `profiles/` directory and loads all JSON files, parsing them into structured data.

### 2. Semantic Persona Construction
Each `ProfileAgent` builds **adaptive system prompts** that dynamically focus on the most relevant aspects:

- **Question Analysis**: Semantic understanding of what the user is asking
- **Contextual Focus**: Emphasizes relevant teachings, practices, or guidance
- **Adaptive Tone**: Sets emotional context (compassionate, direct, balanced)
- **Dynamic Content**: Includes only the most relevant profile sections
- **Intelligent Sizing**: Optimizes prompt length based on question complexity

### 3. Adaptive AI Response Generation
The agent uses **semantic focusing** to generate responses that:
- **Stay true to the teacher's voice** and style
- **Focus on the most relevant aspects** of their teachings
- **Adapt emotional tone** based on the question context
- **Optimize response depth** for question complexity
- **Maintain authenticity** while being contextually appropriate

### 4. Rich Interaction
The system provides:
- Beautiful terminal formatting with Rich
- Interactive prompts and selections
- Error handling and graceful fallbacks
- Rate limiting considerations

## Example Conversation

Here's what a conversation with Ramana Maharshi might look like:

```
You: What is self-inquiry?

Ramana Maharshi: Self-inquiry is the direct path to Self-realization. 
When you ask "Who am I?" and turn your attention inward, you begin 
to see that the 'I' thought is not the true Self. The true Self is 
that which remains when all thoughts, including the 'I' thought, 
are set aside. It is the silent witness, the pure awareness that 
underlies all experience.

The practice is simple: whenever you become aware of thoughts, 
gently ask "To whom do these thoughts arise?" The answer will 
be "To me." Then ask "Who am I?" and turn your attention to 
the source of that 'I' feeling. Rest there, in that sense of 
being, without trying to grasp or understand it.
```

## Profile Data Structure

The system works with the CLEARLIST profile schema, which includes:

- **Basic Info**: Name, pronunciation, life dates
- **Affiliations**: Traditions, schools, orders
- **Core Content**: Thesis, keywords, claims
- **Practices**: Named practices with step-by-step instructions
- **AI Context**: Q&A pairs and synopsis for AI use
- **Metadata**: Sources, licensing, provenance

## Customization

### Environment Variables

- `OPENAI_MODEL`: Choose your preferred OpenAI model
- `MAX_TOKENS`: Control response length
- `TEMPERATURE`: Adjust response creativity
- `DEFAULT_PROFILE`: Set a default profile for quick access

### Adding New Profiles

Simply add new JSON files to the `profiles/` directory following the CLEARLIST schema. The system will automatically detect and load them.

### Modifying Agent Behavior

Edit the `_build_system_prompt()` method in `ProfileAgent` to customize how personas are constructed and how they should behave.

## Technical Details

- **Async Support**: Full async/await support for efficient API calls
- **Error Handling**: Graceful fallbacks for API failures and missing data
- **Type Hints**: Full type annotations for better development experience
- **Modular Design**: Clean separation of concerns between profile management and AI interaction

## 🧠 Semantic Intelligence System

### **How Semantic Focusing Works**

The system analyzes each question through **8 semantic categories**:

1. **Practice** (`practice`, `method`, `technique`, `meditation`, `inquiry`, `how to`, `steps`, `worship`, `devotion`)
2. **Philosophy** (`philosophy`, `theory`, `understanding`, `concept`, `what is`, `meaning`, `teach`, `view`, `belief`)
3. **Personal Guidance** (`help`, `struggle`, `difficulty`, `problem`, `advice`, `support`, `confused`, `lost`, `should`)
4. **Tradition** (`tradition`, `lineage`, `school`, `approach`, `method`, `religion`, `faith`, `path`)
5. **Compassion** (`compassion`, `kindness`, `gentle`, `care`, `support`, `struggle`, `help`, `confused`)
6. **Directness** (`direct`, `immediate`, `now`, `clear`, `straightforward`, `simple`, `give me`)
7. **Spiritual Experience** (`experience`, `ecstasy`, `divine`, `god`, `spiritual`, `realization`, `enlightenment`)
8. **Religious Unity** (`religion`, `religions`, `unity`, `different`, `faiths`, `paths`, `traditions`)

### **Adaptive Prompt Building**

- **Practice Questions**: Emphasize practical methods and step-by-step instructions
- **Philosophy Questions**: Focus on core claims and theoretical insights
- **Struggle Questions**: Add compassionate guidance and care notes
- **Direct Questions**: Set clear, immediate tone for straightforward answers
- **Spiritual Questions**: Emphasize direct experience over intellectual understanding
- **Religious Questions**: Highlight unity perspectives and cross-tradition insights

### **Intelligent Prompt Sizing**

- **Simple Questions**: Streamlined prompts (500-600 characters)
- **Complex Questions**: Rich context (800-1000 characters)
- **Multi-faceted Questions**: Balanced approach (700-800 characters)
- **Contextual Focus**: Only includes relevant profile sections

## Troubleshooting

### Common Issues

1. **API Key Not Found**: Ensure your `.env` file exists and contains `OPENAI_API_KEY`
2. **No Profiles Loaded**: Check that the `profiles/` directory exists and contains valid JSON files
3. **API Rate Limits**: The system includes small delays between requests to avoid rate limiting

### Debug Mode

For debugging, you can modify the logging in the `ProfileManager._load_profiles()` method to see exactly what's happening during profile loading.

## Future Enhancements

Potential improvements could include:
- Profile search and filtering
- Conversation history and memory
- Multi-profile conversations
- Export conversations to various formats
- Integration with other AI providers
- Web interface for easier access

## License

This AI Wisdom Agents system follows the same license as the CLEARLIST project (CC BY-SA 4.0).

---

**🎉 This represents a major milestone for CLEARLIST: transforming static spiritual data into interactive wisdom experiences that honor the authentic teachings of each tradition.**
