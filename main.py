import requests
from dotenv import load_dotenv
import os

# to load environement variables
load_dotenv()

RIOT = os.getenv("RIOT")


LINK = "https://api.henrikdev.xyz/valorant/v1/"

def base_http_request(params):
    # checking if the user wants to check accounts.

    if params == "account":
        try:
            name = input("Please provide name: ")
            tag = input("Please provide tag: ")
            response = requests.get(
                f"{LINK}/{params}/{name}/{tag}",
                headers={"Authorization":RIOT,"Accept":"*/*"},
            )

            if response.status_code != 200:
                print("Player not found")
            else:
                print(response.json())

        except Exception as e:
            print(f"{e.args}")
            print("Failed to get data")


print(RIOT)
base_http_request("account")