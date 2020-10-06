import email
import logging
import mailparser
import pandas as pd
from bs4 import BeautifulSoup as sp
from email.header import decode_header

from emailscraper.parsers.base_email_parser import EmailParser

log = logging.getLogger(__name__)


class SummaryReportEmailParser(EmailParser):
    def extract_application_cat_data(self, all_tbl_list):
        df = df1 = []
        try:
            for in_tbl in all_tbl_list:
                span = in_tbl.find_all("span")
                row = [tr.text for tr in span]
                if row[0] == "Category":
                    df = pd.read_html(str(in_tbl))[0]
                    df = df[df["% Usage"].notna()]
                elif row[0] == "Application":
                    df1 = pd.read_html(str(in_tbl))[0]
                    df1 = df1[df1["% Usage"].notna()]
                    df1 = df1.drop(df1.columns[[1, 2]], axis=1)
        except Exception as e:
            log.error(
                "Issue found in SummaryReportEmailParser.extract_application_cat_data due to:",
                e,
            )
        self.extracted_data["application"] = df
        self.extracted_data["category"] = df1

    def extract_usage_data(self, all_span_list):
        i = j = k = 0
        data_transfer = {}
        data_upload = {}
        data_download = {}
        try:
            for inner_span in all_span_list:
                span_txt = inner_span.text
                if i >= 1 and i < 3:
                    i = i + 1
                    data_transfer[span_txt] = span_txt
                if j >= 1 and j < 3:
                    j = j + 1
                    data_upload[span_txt] = span_txt
                if k >= 1 and k < 3:
                    k = k + 1
                    data_download[span_txt] = span_txt
                if "Total Data Transferred" == span_txt:
                    i = 1
                elif "Total Data Uploaded" == span_txt:
                    j = 1
                elif "Total Data Downloaded" == span_txt:
                    k = 1
        except Exception as e:
            log.error(
                "Issue found in SummaryReportEmailParser.extract_usage_data due to", e
            )
        network_data = {}
        network_data["data_transfer"] = list(data_transfer)
        network_data["data_upload"] = list(data_upload)
        network_data["data_download"] = list(data_download)
        self.extracted_data["network_data"] = network_data

    def extract_subject(self, response):
        try:
            msg = email.message_from_bytes(response[1])
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            ext_sub = subject.split("'")
            network_name = ext_sub[1]
            email_date = ext_sub[2].replace(":", "")
            self.extracted_data["network_name"] = network_name
            self.extracted_data["email_date"] = email_date
        except Exception as e:
            log.error(
                "Issue found in SummaryReportEmailParser.extract_subject due to", e
            )

    def extract_email(self):
        try:
            response = self.email_data
            if isinstance(response, tuple):
                self.extract_subject(response)
                body = mailparser.parse_from_bytes(response[1]).text_html
                soup = sp(body[0], "html.parser")
                all_span_list = soup.find_all("span")
                all_tbl_list = soup.find_all("table")
                self.extract_usage_data(all_span_list)
                self.extract_application_cat_data(all_tbl_list)
        except Exception as e:
            log.error("Issue found in SummaryReportEmailParser.extract_email due to", e)
