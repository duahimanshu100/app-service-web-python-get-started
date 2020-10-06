import logging
from abc import ABCMeta, abstractmethod

log = logging.getLogger(__name__)


class EmailParser(metaclass=ABCMeta):
    def __init__(self, email_data):
        self.extracted_data = {}
        self.email_data = email_data

    @abstractmethod
    def extract_email(self):
        raise NotImplementedError("error message")
