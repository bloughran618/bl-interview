from datetime import datetime
from random import randint
import requests
# retrieve data from /ocpi/sessions endpoint
# GET https://api-dev.chargepass.com/api/1.0/users/charging-sessions/{session_id}
# Headers: Token = eyJ...

# Response:
# {
#     "data": {
#         "status": "INPROGRESS",
#         "elapsed_time": "",
#         "charging_speed": "",
#         "is_presto_pass": true,
#         "total_cost": "",
#         "charge": "0.00",
#         "battery_percentage": "",
#         "range": "",
#         "is_completed": false,
#         "session_id": "35ce2560-78ea-459f-9fdb-6b5e57ed6de1"
#     },
#     "status": true,
#     "status_message": "vehicle charge progress",
#     "timestamp": "2023-06-16T19:42:46.898973592Z"
# }

# Completed:
# {
#     "data": {
#         "status": "INPROGRESS",
#         "elapsed_time": "",
#         "charging_speed": "",
#         "is_presto_pass": true,
#         "total_cost": "",
#         "charge": "0.00",
#         "battery_percentage": "",
#         "range": "",
#         "is_completed": false,
#         "session_id": "c02835d0-1e2a-4cdf-8a73-f27875c1045c"
#     },
#     "status": true,
#     "status_message": "vehicle charge progress",
#     "timestamp": "2023-06-16T20:22:51.004438552Z"
# }


def lambda_handler(event, context):
    # get response using python requests library for endpoint above
    headers = {
        'token': ''
    }
    session_id = event.get("data")[0].get("charge_session_id")
    url = f'https://api-dev.chargepass.com/api/1.0/users/charging-sessions/{session_id}'
    response = requests.get(url, headers=headers)
    data = response.json()

    return {
        "data": data
    }
