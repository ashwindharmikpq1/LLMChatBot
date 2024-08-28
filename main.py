from construct_graph import *
from pprint import pprint
from get_token import set_token


if __name__ == '__main__':
    # set_token()

    # COMPILE
    app = workflow.compile()

    print("==" * 50)
    inputs = {"question": "I want to extend my booking", "phone_number": "8928930667"}
    answer = {}
    for output in app.stream(inputs):
        for key, value in output.items():
            # print(f"key: {key} \t value: {value}")
            # pprint(f"### Finished running: {key} ###")
            answer = value
    print("==" * 50)
    print(f"Answer => \n{answer.get('output', 'ERROR...!!!')}")
    print("==" * 50, "\n")



    # while True:
    #     print("==" * 50)
    #     # Prompt the user for input
    #     user_input = input("\n\nEnter Query (or type 'q' to quit) \n=> ")
    #     # Check if the user entered "q"
    #     if user_input.lower() == 'q':
    #         break
    #
    #     inputs = {"question": user_input}
    #     answer = {}
    #     for output in app.stream(inputs):
    #         for key, value in output.items():
    #             # print(f"key: {key} \t value: {value}")
    #             # pprint(f"### Finished running: {key} ###")
    #             answer = value
    #     print("==" * 50)
    #     print(f"Answer => \n{answer.get('output', 'ERROR...!!!')}")
    #     print("==" * 50, "\n")

# I want to extend my booking by 45 minutes
# 8928930667
