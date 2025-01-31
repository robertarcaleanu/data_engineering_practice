import requests
from classes import auth_param, time_interval
from requests.auth import HTTPBasicAuth


class Extractor:
    def __init__(self, auth: auth_param) -> None:
        self.auth_param = auth

    def get_departures_by_airport(self, airport: str, time_interval: time_interval):
        url = "https://opensky-network.org/api/flights/departure"
        params = {
            "airport": airport,
            "begin": time_interval.begin,
            "end": time_interval.end,
        }
        response = requests.get(
            url,
            params=params,
            auth=HTTPBasicAuth(self.auth_param.username, self.auth_param.password),
        ).json()
        return response

    def get_flights_from_interval(self, time_interval: time_interval):
        url = "https://opensky-network.org/api/flights/all"
        params = {
            "begin": time_interval.begin,
            "end": time_interval.end,
        }
        response = requests.get(
            url,
            params=params,
            auth=HTTPBasicAuth(self.auth.username, self.auth.password),
        ).json()
        return response