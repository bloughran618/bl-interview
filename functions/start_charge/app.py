import requests
# retrieve data from /ocpi/sessions endpoint
# POST https://api-dev.chargepass.com/api/1.0/users/initiate-charge
# Headers: Token = eyJ...
# Body: {
#    "evse_uuid": "a54dbe2b-a51c-4bfc-bebc-59473b1d6292",
#    "station_id": "b25eb58e-6855-4160-bbe6-6b601e229023"
# }

# Response:
# {
#     "data": {
#         "charge_session_id": "e07ec96b-5389-446c-a8a4-1ec596e792a9",
#         "status": "INITIATED",
#         "remote_stop": false
#     },
#     "status": true,
#     "status_message": "Request successfull",
#     "timestamp": "2023-06-15T01:39:13.11752943Z"
# }


def lambda_handler(event, context):
    # get response using python requests library for endpoint above
    headers = {
        'token': ''
    }
    url = f'https://api-dev.chargepass.com/api/1.0/users/initiate-charge'
    body = {
        "evse_uuid": "a54dbe2b-a51c-4bfc-bebc-59473b1d6292",
        "station_id": "b25eb58e-6855-4160-bbe6-6b601e229023"
    }
    response = requests.post(url, body, headers)
    data = response.json()

    if data.get("error"):
        raise RuntimeError("Charge failed")

    return {
        "data": data
    }