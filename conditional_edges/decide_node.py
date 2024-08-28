"""
Based on the retrieved category for the user prompt determine the next Node
e.g. Category: Extension => Next Node: Extension
"""
from manage_env_var import *

def decide_next_node(state):
    """
    Decide the next Node to choose based on category

    Args:
        state(dict) : the current graph state

    Returns:
        str : Binary decision for next node to call
    """
    if debug_ok == "True":
        print("==" * 50)
        print("\n----- NEXT NODE -----")
    question = state["question"]
    category = state["category"]

    return category
