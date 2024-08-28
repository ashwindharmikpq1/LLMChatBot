"""
Based on the query, determine the category (purpose) of the task using the vector database
and categories_filtered.csv file
"""
import chromadb
import pandas as pd
from manage_env_var import *


def load_vector_db():
    if debug_ok == "True":
        print("\t----- LOADING VECTOR DATABASE -----")
    vector_db_path = ("/Users/apple/Desktop/GitLab_Parkquility/REPOSITORY/LLM/LangGraph/chroma_vector_store"
                      "/pq_msgs_dict_v1")
    client = chromadb.PersistentClient(path=vector_db_path)
    collection_name = "pq_msgs_dict_v1"
    collection = client.get_collection(name=collection_name)

    return collection


def category_retriever(collection, prompt):
    if debug_ok == "True":
        print("\t----- RETRIEVE CATEGORY -----")
    results = collection.query(query_texts=prompt, n_results=5)
    # print(f"Result form Collection : {results}")

    res_list = []
    id_list = []
    for i, distance in enumerate(results['distances'][0]):
        # print(f"Distance: {distance}")
        if distance < 0.5:
            res_list.append(results['documents'][0][i])
            id_list.append(results['ids'][0][i])
    # print(f"Doc List: {res_list}")
    # print(f"Id List: {id_list}")

    data = res_list[0]
    category_id = id_list[0]
    # print(f"{id} : {data}")

    csv_file_path = "/Users/apple/Desktop/GitLab_Parkquility/REPOSITORY/LLM/LangGraph/categories_filtered.csv"

    categories_filtered_df = pd.read_csv(csv_file_path)

    # Find the Category for a specific message_body
    category = categories_filtered_df.loc[categories_filtered_df['id'] == int(category_id), 'Sub-Category']

    needed_cat = category.values[0]

    return needed_cat


# if __name__ == '__main__':
#     loaded_collection = load_vector_db()
#
#     user_input = "I want to extend my booking by 45 minutes"
#
#     retrieved_category = category_retriever(loaded_collection, user_input)
#     print(f"Category Selected: {retrieved_category}")
