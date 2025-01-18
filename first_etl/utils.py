from datetime import datetime


def string_to_unix_time(date_string: str, date_format: str = "%Y-%m-%d"):
    # Parse the string into a datetime object
    dt = datetime.strptime(date_string, date_format)

    # Convert the datetime object to Unix time (seconds since the epoch)
    unix_time = int(dt.timestamp())

    return unix_time
