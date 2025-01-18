import os

from classes import auth_param, time_interval
from metadata import AIRPORT, END_DATE, START_DATE
from utils import string_to_unix_time

from first_etl.extract import Extractor


def main():
    auth = auth_param(
        username=os.getenv("OPEN_SKY_USERNAME"), password=os.getenv("OPEN_SKY_PASSWORD")
    )
    response = Extractor(auth).get_departures_by_airport(
        airport=AIRPORT,
        time_interval=time_interval(
            begin=string_to_unix_time(START_DATE), end=string_to_unix_time(END_DATE)
        ),
    )
    print(response)


if __name__ == "main":
    main()
