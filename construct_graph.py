from typing_extensions import TypedDict
from langgraph.graph import END, StateGraph
from nodes.get_category import get_category
from nodes.extend_booking import booking_extension
from conditional_edges.decide_node import decide_next_node


# States - what kind of value do you want to across different steps
class GraphState(TypedDict):
    """
    Represents the state of our graph

    Attributes:
        question: user query
    """
    question: str
    phone_number: str
    category: str
    task_info: dict
    output: str


workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("GetCategory", get_category)
workflow.add_node("ExtendBooking", booking_extension)

# BUILD GRAPH
workflow.set_entry_point("GetCategory")
workflow.add_conditional_edges(
    "GetCategory",
    decide_next_node,
    {
        "extension": "ExtendBooking",
        "NOMATCH": END
    }
)

