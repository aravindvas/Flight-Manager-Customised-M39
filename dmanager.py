import requests
from pprint import pprint
import os

shtend = "https://api.sheety.co/7d4417383a6525d3548aa951e0fc7245/flightDeals/prices2"
uname = "aravindvas"
pasd = "mailme1997"

class DataManager:

    def __init__(self):
        self.des_data = {}

    def get_des_data(self):
        rsp = requests.get(
            url=shtend,
            auth=(
                uname,
                pasd,
            )
        )
        # Basic Authentication
        dt = rsp.json()
        # pprint(dt)
        # print(rsp.status_code)
        self.des_data = dt['prices2']
        return self.des_data

    def upd_des_codes(self):
        for c in self.des_data:
                nw_dt = {
                    "prices2": {
                        "iataCode": c["iataCode"]
                    }
                }

                rsp2 = requests.put(
                    url=f"{shtend}/{c['id']}",
                    auth=(
                        uname,
                        pasd,
                    ),
                    json=nw_dt
                )
                # Basic Authentication
                print(rsp2.status_code)