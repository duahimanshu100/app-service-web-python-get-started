import imaplib
import logging
from django.conf import settings

log = logging.getLogger(__name__)


class ImapClient:
    def __init__(self, email, password):
        try:
            self.imap = imaplib.IMAP4_SSL(settings.IMAP_HOST, 993)
            self.imap.login(email, password)
            self.imap.select("Inbox")
        except Exception as e:
            log.error("Issue found in ImapClient class due to:", e)

    def search(self, query):
        result, data = self.imap.uid("search", query)
        return (result, data)
