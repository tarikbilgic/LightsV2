import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API")
SKU_num = os.getenv("sku")
device = os.getenv("device")



# user_power = input("Do you want to turn the lights on? (Yes/No)").lower().strip()

# if user_power == "yes":
#     global switch
#     switch = 1
# elif user_power == "no":
#     switch = 0 




base_url = "https://openapi.api.govee.com"
control_url = base_url + "/router/api/v1/device/control"
headers={

    "Govee-API-Key": API_KEY,
    "Content-type" : "application/json"

}

brightness_body={

    "requestId": "test1",
    "payload": {

        "sku" : SKU_num,
        "device" : device,
        "capability": {

            "type": "devices.capabilities.range",
            "instance": "brightness",
            "value" : 1
        }
    }
}



def set_brightness(value):
    brightness_body["payload"]["capability"]["value"] = value
    response = requests.post(url=control_url, json=brightness_body, headers=headers)
    data = response.json()
    print(data)


