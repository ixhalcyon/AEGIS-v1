import router
import spinal_answer

def classify_and_route(classification: str, query: str):
    """
    Routes the query to the appropriate module based on the classification.

    Args:
        classification: The classification string (e.g., "REFLEX:CREATIVE").
        query: The user's query.
    """
    q_type, style = classification.split(':')

    if q_type == "REFLEX":
        print(f"Passing query to spinal_answer with style {style}...")
        # Pass query to spinal_answer for simple, short responses
        result = spinal_answer.get_simple_answer(query)
        print(result)
        return result  # Return the result to the caller
    elif q_type == "ROUTE":
        print(f"Passing query to router with style {style}...")
        # The router module decides the style, so we just pass the query
        router.route_query(query)
    else:
        print(f"Unknown classification type: {q_type}")
        # Default behavior or error handling
        print("Defaulting to router.")
        router.route_query(query)
