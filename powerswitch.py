import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API")
SKU_num = os.getenv("sku")
device = os.getenv("device")

is_on = False

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

power_on={

    "requestId": "test1",
    "payload": {

        "sku" : SKU_num,
        "device" : device,
        "capability": {

            "type": "devices.capabilities.on_off",
            "instance": "powerSwitch",
            "value": 1
        }
    }
}


power_off={

    "requestId": "test1",
    "payload": {

        "sku" : SKU_num,
        "device" : device,
        "capability": {

            "type": "devices.capabilities.on_off",
            "instance": "powerSwitch",
            "value": 0
        }
    }
}






# response = requests.get(url, headers=headers)
# data = response.json()

def powerswitch():
    global is_on
    if is_on == False:
        power = requests.post(url=control_url, json=power_on, headers=headers)
        data = power.json()

    elif is_on == True:
        power = requests.post(url=control_url, json= power_off, headers=headers)
        data = power.json()

    if power.ok: 
        is_on = not is_on
    
    return is_on
    


