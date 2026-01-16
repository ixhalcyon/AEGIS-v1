#!/usr/bin/env python3
"""
entry.py

Terminal user interface that takes user queries, passes them to query_handler.py,
and displays refined answers from refinery.py.
"""

import sys
import os
import subprocess
import io
from contextlib import redirect_stdout, redirect_stderr

# Add the REFINERY directory to the Python path to import refinery
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'REFINERY'))

# Import refinery module
import refinery


def run_query_handler(user_query):
    """
    Simulates passing the query to query_handler.py by replicating its functionality.
    This avoids subprocess complexity while maintaining the intended flow.
    """
    import db
    import spinal_code
    
    # Make sure the table exists
    db.create_table()
    
    # Get classification result
    result = spinal_code.classify_query(user_query)
    
    # Save the query and result to the database
    db.save_query(user_query, result)
    
    print(f"Query: '{user_query}'")
    print(f"Classification: {result}")
    print("--- Query saved to database. ---")
    
    # Execute the query (this calls spinal_code.execute_query)
    execution_result = spinal_code.execute_query(result, user_query)

    return result, execution_result


def main():
    """
    Main function that handles the user interface.
    Takes user queries, processes them through the system, and displays refined answers.
    """
    print("Welcome to AEGIS Terminal Interface!")
    print("This system will:")
    print("1. Process your query through the classification system")
    print("2. Generate both creative and logical responses")
    print("3. Refine the responses for better quality")
    print("Type 'exit' to quit.")
    
    while True:
        user_query = input("Enter your query (or 'exit' to quit): ")
        
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        
        if not user_query.strip():
            print("Please enter a valid query.")
            continue

        print("\nProcessing your query through the classification system...\n")

        # Process query through the classification system (similar to query_handler.py)
        try:
            classification_result, execution_result = run_query_handler(user_query)
            print(f"\nClassification completed: {classification_result}")

            # If execution_result is from spinal_answer (simple answer), display it directly
            if execution_result is not None and isinstance(execution_result, str):
                print("\n==================== SIMPLE ANSWER ====================")
                print(f"INPUT: {user_query}")
                print(f"ANSWER: {execution_result}")
                print("=========================================================\n")
            else:
                print("\nGenerating refined responses...\n")

                # Get refined responses from refinery.py
                refined_result = refinery.get_refined_responses(user_query)

                # Display the refined responses
                print("\n==================== REFINED RESPONSES ====================")
                print(f"ORIGINAL INPUT: {user_query}")
                print("\n--- ORIGINAL CREATIVE RESPONSE ---")
                print(refined_result['original']['creative'])
                print("\n--- REFINED CREATIVE RESPONSE ---")
                print(refined_result['refined']['refined_creative'])
                print("\n--- ORIGINAL LOGICAL RESPONSE ---")
                print(refined_result['original']['logical'])
                print("\n--- REFINED LOGICAL RESPONSE ---")
                print(refined_result['refined']['refined_logical'])
                print("\n=========================================================\n")

        except Exception as e:
            print(f"An error occurred while processing your query: {e}")
            import traceback
            traceback.print_exc()

        print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    main()
