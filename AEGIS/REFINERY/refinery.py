#!/usr/bin/env python3
"""
refinery.py

Takes results from receiver.py and refines/polishes the output using an AI model via OpenRouter API.
"""

import sys
import os
from openai import OpenAI

# Add the Main_aegis directory to the Python path to import receiver
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Main_aegis'))

# Import the receiver module
import receiver

# WARNING: Hardcoding API keys is not recommended for production environments.
# For better security, consider using environment variables or a secure configuration management system.
api_key = "YOUR_OPENROUTER_API_KEY"

# Instantiate the client, pointing it to the OpenRouter API endpoint
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# A prompt that instructs the AI to refine and polish responses
refinement_prompt = """You are an expert editor and content refiner. Your task is to take the provided responses and polish them to improve clarity, coherence, and overall quality. Follow these guidelines:

1. Maintain the original meaning and intent of the responses
2. Improve grammar, spelling, and punctuation
3. Enhance readability and flow
4. Make the content more concise where possible without losing important information
5. Ensure the refined content is well-structured and professional
6. For creative responses, preserve the imaginative elements while improving the presentation
7. For logical responses, ensure the reasoning remains clear and well-organized
8. Correct any factual inaccuracies if present
9. Make the language more engaging and polished
10. Ensure the refined content is appropriate for a general audience

Please refine the following responses:"""

def refine_response(input_text):
    """
    Calls the AI model with a specific prompt to refine and polish the response.

    Args:
        input_text: The text to be refined.

    Returns:
        The AI's refined response.
    """
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # Using a reliable model
            messages=[
                {"role": "system", "content": refinement_prompt},
                {"role": "user", "content": input_text},
            ],
            temperature=0.5,
        )
        if response.choices:
            return response.choices[0].message.content
        return "No refined response generated."
    except Exception as e:
        return f"An error occurred during refinement: {e}"


def refine_both_responses(user_input, creative_response, logical_response):
    """
    Refines both creative and logical responses.

    Args:
        user_input: The original user input.
        creative_response: The creative AI response to refine.
        logical_response: The logical AI response to refine.

    Returns:
        A dictionary containing both refined creative and logical responses.
    """
    # Combine the original input with each response for better context
    creative_context = "Original Question: " + user_input + "\n\nCreative Response: " + creative_response
    logical_context = "Original Question: " + user_input + "\n\nLogical Response: " + logical_response
    
    refined_creative = refine_response(creative_context)
    refined_logical = refine_response(logical_context)
    
    return {
        "refined_creative": refined_creative,
        "refined_logical": refined_logical
    }


def get_refined_responses(user_input):
    """
    Gets responses from receiver and then refines them.

    Args:
        user_input: The user's question or statement.

    Returns:
        A dictionary containing both original and refined creative and logical responses.
    """
    # Get responses from receiver
    original_responses = receiver.get_both_responses(user_input)
    
    # Refine the responses
    refined_responses = refine_both_responses(
        user_input,
        original_responses["creative"],
        original_responses["logical"]
    )
    
    # Combine original and refined responses
    result = {
        "original": original_responses,
        "refined": refined_responses
    }
    
    return result


def display_refined_responses(user_input, responses):
    """
    Displays both original and refined responses in a formatted way.

    Args:
        user_input: The original user input.
        responses: Dictionary containing original and refined responses.
    """
    print("")
    print("--- Original Input ---")
    print("Q: " + user_input)
    
    print("")
    print("--- Original Creative Response ---")
    print("A: " + responses['original']['creative'])
    
    print("")
    print("--- Refined Creative Response ---")
    print("A: " + responses['refined']['refined_creative'])
    
    print("")
    print("--- Original Logical Response ---")
    print("A: " + responses['original']['logical'])
    
    print("")
    print("--- Refined Logical Response ---")
    print("A: " + responses['refined']['refined_logical'])


if __name__ == "__main__":
    print("Refinery: Response Refinement System")
    print("Type 'exit' to quit.")
    print("")
    
    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() == 'exit':
            break
            
        responses = get_refined_responses(user_input)
        display_refined_responses(user_input, responses)
        print("")
        print("="*70)
        print("")
