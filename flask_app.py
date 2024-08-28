from flask import Flask, jsonify, request
from construct_graph import *

app = Flask(__name__)


# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Define an API endpoint
@app.route('/llm/chatbot/', methods=['GET'])
def run_llm():
    # Get the query parameters as a dictionary
    params_dict = request.args.to_dict()

    # result = {'message': 'Received dictionary: {}'.format(params_dict)}
    # return jsonify(result)

    pq_chatbot = workflow.compile()

    answer = {}
    for output in pq_chatbot.stream(params_dict):
        for key, value in output.items():
            # print(f"key: {key} \t value: {value}")
            # pprint(f"### Finished running: {key} ###")
            answer = value

    # return answer.get('output', 'ERROR...!!!')
    return jsonify({"Response": answer.get('output', 'ERROR...!!!')}), 201

# # Another endpoint to handle POST requests
# @app.route('/api/data', methods=['POST'])
# def create_data():
#     if request.is_json:
#         data = request.get_json()
#         return jsonify({"message": "Data received", "data": data}), 201
#     else:
#         return jsonify({"error": "Request must be JSON"}), 400


if __name__ == '__main__':
    app.run(debug=True)


# curl -X GET 'http://localhost:5000/api?question=I want to extend my booking&phone_number=8928930667'
# {"question": "I want to extend my booking", "phone_number": "8928930667"}
