import json
from functions.apis import get_valet_bookings
from manage_env_var import *


def get_user_bookings(phone: str):
    """For the given phone number, fetch the bookings for the user. Return list of bookings."""
    if debug_ok == "True":
        print("==" * 50)
        print("\n----- FETCH USER BOOKINGS -----")
    bookings = get_valet_bookings(phone)
    # print(f"bookings : {bookings}")
    if bookings:
        bookings_data = bookings["data"]
        return bookings_data

    else:
        # print("No bookings with this phone number")
        return None

# def get_user_bookings(phone: str) -> list:
#     """For the given phone number, fetch the bookings for the user. Return list of bookings."""
#     print("==" * 50)
#     print("\n----- FETCH USER BOOKINGS -----")
#     bookings = get_valet_bookings(phone)
#     # print(f"bookings : {bookings}")
#     if bookings:
#         bookings_data = bookings["data"]  # ["bookings"]
#         selected_list = [item for item in bookings_data if item["contact_number"] == phone]
#
#         # k_list = ['booking_id', 'vehicle_no', 'status', 'first_name', 'last_name', 'arena_name', 'slot_name',
#         #           'booking_start_time_str', 'booking_end_time_str', 'actual_booking_start_time_str',
#         #           'actual_booking_end_time_str', 'contact_number']
#         k_list = ['booking_id', 'vehicle_no', 'status', 'arena_name', 'actual_booking_start_time_str',
#                   'actual_booking_end_time_str']
#
#         show_selected_list = []
#         booking_id_list = []
#         for item in selected_list:
#             booking_id_list.append(item["booking_id"])
#             temp_dict = {}
#             for key in k_list:
#                 value = item[key]
#                 temp_dict[key] = value
#             show_selected_list.append(temp_dict)
#
#         # print("\nUser Bookings Summery =>")
#         # for booking_entry in show_selected_list:
#         #     print(f"{json.dumps(booking_entry, indent=4)}")
#
#         return booking_id_list
#
#     else:
#         print("No bookings with this phone number")
#         return []


if __name__ == "__main__":
    resp = get_user_bookings("8928930667")
