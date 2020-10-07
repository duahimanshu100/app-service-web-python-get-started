import dateutil
from datetime import datetime, timedelta


def convert_str_to_date(str_date, date_format="%Y-%m-%d"):
    date_obj = dateutil.parser.parse(str_date)
    return datetime.strftime(date_obj, date_format)


def get_current_date_time():
    return datetime.now()

def get_previous_date_time(date_format="%d-%b-%Y"):
    previous_date = datetime.today() - timedelta(days=1)
    return datetime.strftime(previous_date, date_format)