import db
import spinal_code

def main():
    """
    This function takes a user's query, classifies it, saves it to the DB,
    and prints the result.
    """
    # Make sure the table exists
    db.create_table()

    user_query = input("Please enter your query: ")

    # Get classification result
    result = spinal_code.classify_query(user_query)

    # Save the query and result to the database
    db.save_query(user_query, result)

    print(f"Query: '{user_query}'")
    print(f"Result: {result}")
    print("--- Query saved to database. ---")

    # Execute the query
    spinal_code.execute_query(result, user_query)

if __name__ == "__main__":
    main()
