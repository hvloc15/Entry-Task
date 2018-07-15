from datetime import datetime


def to_timestamp(dt):
    return (dt - datetime(1970, 1, 1)).total_seconds()


def string_to_timestamp(date_str,date_format="%d-%m-%Y"):
    return to_timestamp(datetime.strptime(date_str,date_format))