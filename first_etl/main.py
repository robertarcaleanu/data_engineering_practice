import os

from first_etl.classes import auth_param, time_interval
from first_etl.first_etl.extract import Extractor
from first_etl.metadata import AIRPORT, END_DATE, START_DATE
from first_etl.utils import string_to_unix_time


def main():
    auth = auth_param(
        username=os.getenv("OPEN_SKY_USERNAME"), password=os.getenv("OPEN_SKY_PASSWORD")
    )
    response = Extractor(auth).get_departures_by_airport(
        airport=AIRPORT,
        time_interval=time_interval(
            begin=string_to_unix_time(START_DATE, "%Y-%m-%d %H:%M:%S"), end=string_to_unix_time(END_DATE, "%Y-%m-%d %H:%M:%S")
        ),
    )
    print(response)


if __name__ == "main":
    main()
