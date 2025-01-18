import requests
from classes import auth_param, time_interval
from requests.auth import HTTPBasicAuth


class Extractor:
    def __init__(self, auth: auth_param) -> None:
        self.auth_param = auth

    def get_departures_by_airport(self, airport: str, time_interval: time_interval):
        url = "https://opensky-network.org/api/flights/arrival"
        params = {
            "airport": airport,
            "begin": time_interval.begin,
            "end": time_interval.end,
        }
        return requests.get(
            url,
            params=params,
            auth=HTTPBasicAuth(self.auth.username, self.auth.password),
        ).json()
