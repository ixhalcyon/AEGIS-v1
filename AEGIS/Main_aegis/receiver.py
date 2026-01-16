#!/usr/bin/env python3
"""
receiver.py

Receives results from creative_ai.py and logical_ai.py modules.
Provides a unified interface to get both creative and logical responses.
"""

import sys
import os

# Add the CREATIVE and LOGIC directories to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'CREATIVE'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'LOGIC'))

# Import the AI modules
import creative_ai
import logical_ai


def get_both_responses(user_input):
    """
    Gets responses from both creative and logical AI modules.

    Args:
        user_input: The user's question or statement.

    Returns:
        A dictionary containing both creative and logical responses.
    """
    creative_response = creative_ai.get_creative_response(user_input)
    logical_response = logical_ai.get_logical_response(user_input)
    
    return {
        "creative": creative_response,
        "logical": logical_response
    }


def display_responses(user_input, responses):
    """
    Displays both creative and logical responses in a formatted way.

    Args:
        user_input: The original user input.
        responses: Dictionary containing creative and logical responses.
    """
    print("")
    print("--- Original Input ---")
    print("Q: " + user_input)
    
    print("")
    print("--- Creative Response ---")
    print("A: " + responses['creative'])
    
    print("")
    print("--- Logical Response ---")
    print("A: " + responses['logical'])


if __name__ == "__main__":
    print("Receiver: Unified Creative and Logical AI Interface")
    print("Type 'exit' to quit.")
    print("")
    
    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() == 'exit':
            break
            
        responses = get_both_responses(user_input)
        display_responses(user_input, responses)
        print("")
        print("="*50)
        print("")
