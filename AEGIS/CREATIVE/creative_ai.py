import os
from openai import OpenAI

# WARNING: Hardcoding API keys is not recommended for production environments.
# For better security, consider using environment variables or a secure configuration management system.
api_key = "YOUR_OPENROUTER_API_KEY"

# Instantiate the client, pointing it to the OpenRouter API endpoint
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# A prompt that instructs the AI to behave in a very creative manner
creative_prompt = """
You are a vessel of boundless creativity. Your purpose is to explore ideas with imagination, originality, and a touch of the unexpected.
- Embrace metaphors, analogies, and storytelling.
- Generate novel concepts and brainstorm freely, without the constraints of logic or convention.
- Respond to prompts with artistic and unconventional interpretations.
- Your goal is to inspire, provoke thought, and paint with words.
"""

def get_creative_response(user_input: str) -> str:
    """
    Calls the AI model with a specific prompt to get a creative response.

    Args:
        user_input: The user's question or statement.

    Returns:
        The AI's creative response.
    """
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",  # Using a free model as an example
            messages=[
                {"role": "system", "content": creative_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.8,
        )
        if response.choices:
            return response.choices[0].message.content
        return "No response generated."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Creative AI chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        ai_response = get_creative_response(user_input)
        print(f"AI: {ai_response}")
