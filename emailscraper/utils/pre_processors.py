import logging
from cis.utils.date import get_current_date_time, convert_str_to_date
from emailscraper.utils.utils import get_usage_in_mb, get_clinic_macadd
from django.conf import settings

log = logging.getLogger(__name__)


def preprocess_network_usage(network_data, network_name, email_date) -> dict:
    response = {}
    try:
        ssid = get_clinic_macadd(network_name)
        data_trans = network_data.get("data_transfer")
        data_down = network_data.get("data_download")
        data_upload = network_data.get("data_upload")
        current_date = get_current_date_time()
        response["ssid_mac_address"] = ssid.mac_address
        response["clinic_id"] = ssid.clinic_id
        response["total_data_transferred"] = get_usage_in_mb(
            data_trans[0], data_trans[1]
        )
        response["total_data_downloaded"] = get_usage_in_mb(data_down[0], data_down[1])
        response["total_data_uploaded"] = get_usage_in_mb(
            data_upload[0], data_upload[1]
        )
        response["data_unit"] = settings.DATA_UNIT
        response["email_date"] = convert_str_to_date(email_date)
        response["created_by"] = settings.USER_NAME
        response["created_date"] = current_date
        response["modified_by"] = settings.USER_NAME
        response["modified_date"] = current_date
    except Exception as e:
        log.error("Issue found in preprocess_network_usage function due to:", e)
    return response


def preprocess_application_usage(application, network_name, email_date) -> dict:
    response = []
    try:
        ssid = get_clinic_macadd(network_name)
        current_date = get_current_date_time()
        clinic_id = ssid.clinic_id
        mac_address = ssid.mac_address
        for i in range(len(application)):
            inner_dct = {}
            usage = application.iloc[i, 1].replace(u"\xa0", u" ").split(" ")
            inner_dct["ssid_mac_address"] = mac_address
            inner_dct["clinic_id"] = clinic_id
            inner_dct["application_name"] = application.iloc[i, 0]
            inner_dct["usage"] = get_usage_in_mb(usage[0], usage[1])
            inner_dct["data_unit"] = settings.DATA_UNIT
            inner_dct["email_date"] = convert_str_to_date(email_date)
            inner_dct["created_by"] = settings.USER_NAME
            inner_dct["created_date"] = current_date
            inner_dct["modified_by"] = settings.USER_NAME
            inner_dct["modified_date"] = current_date
            response.append(inner_dct)
    except Exception as e:
        log.error("Issue found in preprocess_application_usage function due to:", e)
    return response


def preprocess_socialmedia(category) -> dict:
    current_date = get_current_date_time()
    response = []
    try:
        for i in range(len(category)):
            inner_dct = {}
            inner_dct["application_name"] = category.iloc[i, 0]
            inner_dct["is_active"] = 0
            inner_dct["is_socialmedia_app"] = 0
            inner_dct["created_by"] = settings.USER_NAME
            inner_dct["created_date"] = current_date
            inner_dct["modified_by"] = settings.USER_NAME
            inner_dct["modified_date"] = current_date
            response.append(inner_dct)
    except Exception as e:
        log.error("Issue found in preprocess_socialmedia function due to:", e)
    return response
