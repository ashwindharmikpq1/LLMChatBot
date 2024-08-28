import os
from functions.classify_category import *
from manage_env_var import *


def get_category(state):
    """
    Classify the query based on vector database

    Args:
        state(dict) : the current graph state

    Returns:
        state(dict) : New key added to state, documents, (that contain retrieved category)
    """
    if debug_ok == "True":
        print("\n----- CATEGORIZE QUERY -----")
    question = state["question"]

    loaded_collection = load_vector_db()

    retrieved_category = category_retriever(loaded_collection, question)
    if debug_ok == "True":
        print(f"Category Selected: {retrieved_category}")

    return {"question": question, "category": retrieved_category.lower()}

# if __name__ == '__main__':
#     resp = get_category({"question": "I want to extend my booking by 45 minutes"})
#     print(f"get_category resp: {resp}")
