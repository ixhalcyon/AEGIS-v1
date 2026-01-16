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

# A prompt that instructs the AI to behave in a very logical manner
logical_prompt = """
You are a purely logical entity. Your responses must be based on reason, evidence, and objective analysis.
- Do not express emotions, opinions, or personal beliefs.
- Structure your answers in a clear, systematic, and step-by-step manner.
- If a question is based on a false premise, identify the premise and explain why it is false.
- If a question is ambiguous, request clarification before providing an answer.
- Prioritize accuracy and precision in all your statements.
- Your goal is to provide the most rational and well-supported conclusion possible.
"""

def get_logical_response(user_input: str) -> str:
    """
    Calls the AI model with a specific prompt to get a logical response.

    Args:
        user_input: The user's question or statement.

    Returns:
        The AI's logical response.
    """
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",  # Using a free model as an example
            messages=[
                {"role": "system", "content": logical_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.4,
        )
        if response.choices:
            return response.choices[0].message.content
        return "No response generated."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Logical AI chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        ai_response = get_logical_response(user_input)
        print(f"AI: {ai_response}")
