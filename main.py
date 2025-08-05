import requests
from dotenv import load_dotenv
import os
import hen

# to load environement variables
load_dotenv()

RIOT = os.getenv("RIOT")


LINK = "https://api.henrikdev.xyz/valorant/v1/"

henn = hen.HenrikDevClient(RIOT)

print(henn._get("account", name="GoTyOsTorA", tag="GO"))
print(henn.get_account(name="GoTyOsTorA", tag="GOT"))