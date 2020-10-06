import logging
from django.conf import settings

from emailscraper.imap_client import ImapClient
from emailscraper.parsers.summary_report_email_parser import SummaryReportEmailParser
from emailscraper.utils.pre_processors import preprocess_network_usage, preprocess_application_usage, \
    preprocess_socialmedia
from emailscraper.utils.utils import create_network_usage, create_application_usage, create_socialmedia

log = logging.getLogger(__name__)


def email_processing():
    try:
        imap_client = ImapClient(settings.SCRAPING_EMAIL, settings.SCRAPING_PASSWORD)
        result, data = imap_client.search('(SINCE "20-SEP-2020")')
        number_of_emails = len(data[0].split())
        for email_index in range(number_of_emails):
            latest_email_uid = data[0].split()[email_index]
            result, email_data = imap_client.imap.uid(
                "fetch", latest_email_uid, "(RFC822)"
            )
            summary_report = SummaryReportEmailParser(email_data[0])
            summary_report.extract_email()
            dict_data: dict = summary_report.extracted_data
            network = preprocess_network_usage(
                dict_data["network_data"],
                dict_data["network_name"],
                dict_data["email_date"],
            )
            create_network_usage(network)
            applications = preprocess_application_usage(
                dict_data["application"],
                dict_data["network_name"],
                dict_data["email_date"],
            )
            for application in applications:
                create_application_usage(application)
            socialmedias = preprocess_socialmedia(dict_data["category"])
            for socialmedia in socialmedias:
                create_socialmedia(socialmedia)
    except Exception as e:
        log.error(
            "There was in error in processing network usage statistics, with an error message:",
            e,
        )
        raise e
