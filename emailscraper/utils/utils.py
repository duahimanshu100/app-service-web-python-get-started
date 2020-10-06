import logging
from django.conf import settings

from emailscraper.imap_client import ImapClient
from emailscraper.parsers.summary_report_email_parser import SummaryReportEmailParser
from emailscraper.models import (
    NetworkUsageStatistics,
    ApplicationUsageStatistics,
    VenueSocialMediaApplications,
    Ssids,
)

log = logging.getLogger(__name__)


def get_usage_in_mb(usage, utype):
    metricInMB = "0.0"
    try:
        if utype == "KB":
            metricInMB = round(float(usage) / 1024, 2)
        elif utype == "GB":
            metricInMB = float(usage) * 1024
        elif utype == "MB":
            metricInMB = float(usage)
    except Exception as e:
        log.error("Issue found in converting usage to MB", e)
    return metricInMB


def get_clinic_macadd(ssid):
    result = []
    try:
        result = Ssids.objects.get(ssid__iexact=ssid)
    except Ssids.DoesNotExist:
        log.error("Ssids does not exists for:", ssid)
    return result


def create_network_usage(data: dict):
    netusage_obj = NetworkUsageStatistics(**data)
    netusage_obj.save()


def create_application_usage(data: dict):
    apl_usage_obj = ApplicationUsageStatistics(**data)
    apl_usage_obj.save()


def create_socialmedia(data: dict):
    venue_obj = VenueSocialMediaApplications(**data)
    venue_obj.save()



