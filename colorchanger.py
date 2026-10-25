import requests
from dotenv import load_dotenv
import os
import color
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


colour_change= {

    "requestId": "test1",
    "payload": {
        "sku" : SKU_num,
        "device" : device,
        "capability": {

            "type": "devices.capabilities.color_setting",
            "instance": "colorRgb",
            "value" : {}
        }


    }


}








def change_colour(choice):
    if choice in color.COLOURS:
        number = color.COLOURS[choice]

    else:
        print("Invalid Colour")




def send_colour(number):

    colour_change= {

    "requestId": "test1",
    "payload": {
        "sku" : SKU_num,
        "device" : device,
        "capability": {

            "type": "devices.capabilities.color_setting",
            "instance": "colorRgb",
            "value" : number
            }


        }


    }   
    response = requests.post(url=control_url, json=colour_change, headers=headers, timeout=10)
    return response

