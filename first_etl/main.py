import os

from classes import auth_param, time_interval
from extract import Extractor
from load import Loader
from metadata import AIRPORT, END_DATE, START_DATE
from transform import Transformer
from utils import string_to_unix_time


def main():
    auth = auth_param(
        username=os.getenv("OPEN_SKY_USERNAME"), password=os.getenv("OPEN_SKY_PASSWORD")
    )
    response = Extractor(auth).get_departures_by_airport(
        airport=AIRPORT,
        time_interval=time_interval(
            begin=string_to_unix_time(START_DATE, "%Y-%m-%d %H:%M:%S"),
            end=string_to_unix_time(END_DATE, "%Y-%m-%d %H:%M:%S"),
        ),
    )
    df = Transformer().transform(source=response)
    Loader().load_data(df)
    success = True
    return success


if __name__ == "__main__":
    main()
