import requests
import json

def get_simple_answer(query: str) -> str:
    """
    Uses Ollama AI model to answer the query with a simple and short response.
    
    Args:
        query: The user's query to be answered.
        
    Returns:
        A simple, short answer from the AI model.
    """
    # Ollama API endpoint
    url = "http://localhost:11434/api/generate"
    
    # Craft the prompt to ensure simple and short answers
    prompt = f"Answer very simply and in short: {query}"
    
    # Payload for the API request
    payload = {
        "model": "smollm:135m",  # Using smollm:135m as default, can be changed as needed
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1  # Lower temperature for more consistent, focused answers
        }
    }
    
    try:
        # Make the POST request to Ollama API
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            
            # Extract the answer from the response
            answer = result.get('response', 'Sorry, I could not generate an answer.')
            
            return answer.strip()
        else:
            return f"Error: Received status code {response.status_code} from Ollama API."
    
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama API: {str(e)}"
    except json.JSONDecodeError:
        return "Error: Invalid response format from Ollama API."
    except Exception as e:
        return f"Unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    query = "What is the capital of France?"
    answer = get_simple_answer(query)
    print(f"Query: {query}")
    print(f"Answer: {answer}")
