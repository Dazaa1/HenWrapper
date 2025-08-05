import requests
import os
import utils

class HenrikDevClient:
    def __init__(self, api_key, base_url="https://api.henrikdev.xyz/valorant/v1"):
        self.__base_url = base_url
        self.api_key = api_key

    # the getter for base_url
    @property
    def base_url(self):
        return self.__base_url    


    # the setter
    @base_url.setter
    def base_url(self, value):
        if len(value) <= 0:
            raise ValueError("We need a url")
        
        elif not isinstance(value, str):
            raise TypeError("url must be a string")
        
        self.__base_url = value

    # defining the _get() helper method
    def _get(self, endpoint, **kwargs):
        if endpoint == "account":
            name = kwargs["name"]
            tag = kwargs["tag"]
            response = requests.get(
                f"{self.__base_url}/{endpoint}/{name}/{tag}",
                headers={"Authorization":self.api_key,"Accept":"*/*"},
            )

            utils.response_handler(response)
            
        return response.json()

    def get_account(self, name, tag):
        return self._get("account", name, tag)
