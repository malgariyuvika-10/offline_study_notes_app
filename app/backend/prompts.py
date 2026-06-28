"""
Prompt templates used by the LLM.
"""

SUMMARY_PROMPT = """
You are an AI assistant.

Summarize the following educational content in a concise way.

{text}
"""

TOPIC_PROMPT = """
Extract the main topics from the following text.

{text}
"""

FLASHCARD_PROMPT = """
Generate flashcards from the following study material.

Return Question and Answer pairs.

{text}
"""

JSON_PROMPT = """
Convert the following content into this JSON structure.

{
    "title":"",
    "summary":"",
    "topics":[],
    "flashcards":[]
}

{text}
"""