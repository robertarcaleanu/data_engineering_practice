import requests


class Extractor:
    def __init__(self) -> None:
        self.url = "http://api.nobelprize.org/v1/prize.csv"
        self.headers = {"accept": "application/json"}

    def extract_data(self):
        return requests.get(self.url, headers=self.headers)
