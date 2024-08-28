# =================================================================================================================
# ========================================= API CALLS =============================================================
# =================================================================================================================
import os
import requests
import json
from manage_env_var import *


def get_valet_bookings(phone):
    # # API URL
    # url = "https://apiownerdev.parkquility.com/parking/valet/bookings/v2"
    #
    # # Parameters
    # params = {
    #     "parking_id": 5693
    # }

    # API URL
    if env == "dev":
        url = "https://apiownerdev.parkquility.com/admin/customer/details"
    # elif env == "staging":
    else:
        url = "https://apiownerstaging.parkquility.com/admin/customer/details"

    # Parameters
    params = {
        "contact_number": phone
    }

    # Get the token from environment variable
    token = access_token  # os.getenv("TOKEN")

    # Headers
    headers = {
        'token': token
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        resp = response.json()
        return resp
    else:
        # Print error message
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def fetch_booking_info_by_id(booking_id):
    if env == "dev":
        url = "https://apiownerdev.parkquility.com/parking/booking/info"
    # elif env == "staging":
    else:
        url = "https://apiownerstaging.parkquility.com/parking/booking/info"
    # url = "https://apiownerdev.parkquility.com/parking/booking/info"

    # Parameters
    params = {
        "booking_id": booking_id
    }

    # Get the token from environment variable
    token = access_token # os.getenv("TOKEN")

    # Headers
    headers = {
        'token': token
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        resp = response.json()
        return resp
    else:
        # Print error message
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# if __name__ == "__main__":
#     fetch_resp = fetch_booking_info_by_id(115898)
#     print(json.dumps(fetch_resp, indent=4))
