import datetime
import json
import os

from functions.get_bookings import get_user_bookings
from functions.apis import fetch_booking_info_by_id
from manage_env_var import *


# def get_phone_number(state):
#     """ Pause the graph after sending the msg asking for phone number """
#     print("\n----- GET USER CONTACT -----")
#     phone_number = "Please enter your phone number => "
#     # send the msg to the number where the query came from
#
#
# def get_booking_id(state):
#     """ Pause the graph after sending the msg asking for booking_id """
#     print("\n----- GET BOOKING ID -----")
#     booking_id = "Please select a booking to extend (enter the booking id) => "
#     # send the msg to the number where the query came from


# def booking_extension(state):
#     print("\n----- EXTEND USER BOOKING -----")
#     phone_number = input("\nPlease enter your phone number => ")
#
#     user_bookings = get_user_bookings(phone_number)
#     # return user_bookings
#
#     booking_id = input("\nPlease select a booking to extend (enter the booking id) => ")
#
#     bookings_data = fetch_booking_info_by_id(booking_id)
#     selected_booking_hash = bookings_data["data"]["hash"]
#
#     extension_link = f"https://stagingpay.parkquility.com/view?hash={selected_booking_hash}&env=dev"
#
#     return {"output": f"Please use this link to extend your booking: {extension_link}"}

def booking_extension(state):
    if debug_ok == "True":
        print("\n----- EXTEND USER BOOKING -----")
    phone_number = state["phone_number"]

    user_bookings = get_user_bookings(phone_number)
    # print(json.dumps(user_bookings, indent=4))

    if user_bookings:
        most_recent_booking = max(user_bookings,
                                  key=lambda x: datetime.datetime.strptime(x['booking_start_time_str'],
                                                                           '%b %d, %Y, %I:%M %p'))
        # print(json.dumps(most_recent_booking, indent=4))

        booking_status = most_recent_booking["status"]
        if booking_status.lower() == "ongoing":
            booking_id = most_recent_booking["booking_id"]
            # print(f"most recent booking id: {booking_id}")
        else:
            return {"output": f"There are no ongoing bookings for {phone_number}."}

        bookings_data = fetch_booking_info_by_id(booking_id)
        # print(json.dumps(bookings_data, indent=4))

        selected_booking_hash = bookings_data["data"]["hash"]

        # extension_link = f"https://stagingpay.parkquility.com/view?hash={selected_booking_hash}&env=dev"
        if env == "dev":
            extension_link = f"https://stagingpay.parkquility.com/view?hash={selected_booking_hash}&env=dev"
        # elif env == "staging":
        else:
            extension_link = f"https://stagingpay.parkquility.com/view?hash={selected_booking_hash}"

        return {"output": f"Please use this link to extend your booking: {extension_link}"}

    else:
        return {"output": f"There are no bookings for {phone_number}."}

# if __name__ == "__main__":
#     resp = booking_extension()
#     print(f"\nPlease use this link to extend your booking: {resp}")
