import requests

url = "http://localhost:5000/" + "llm/chatbot/"
params = {
    "question": "I want to extend my booking",
    "phone_number": "8928930667"
}

response = requests.get(url, params=params)

print("Response Status Code:", response.status_code)
print("Response Content:=> \n", response.text)
