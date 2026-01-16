import sys
import os

# Add the parent directory of CREATIVE and LOGIC to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'CREATIVE')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'LOGIC')))


from CREATIVE.creative_ai import get_creative_response
from LOGIC.logical_ai import get_logical_response

def route_query(query: str):
    """
    Routes the query to the appropriate AI based on keywords.

    Args:
        query: The user's query.
    """
    if "CREATIVE" in query.upper():
        print("Routing to Creative AI...")
        response = get_creative_response(query)
        print(f"Creative AI says: {response}")
    elif "LOGIC" in query.upper():
        print("Routing to Logical AI...")
        response = get_logical_response(query)
        print(f"Logical AI says: {response}")
    else:
        print("No keyword found, using default AI.")
        # As a default, you might want to choose one, or have a general purpose AI
        # For this example, let's default to logical
        response = get_logical_response(query)
        print(f"Logical AI says: {response}")

if __name__ == "__main__":
    while True:
        user_query = input("Enter your query (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        route_query(user_query)
