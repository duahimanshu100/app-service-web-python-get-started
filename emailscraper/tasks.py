from cis.celery import app
from emailscraper.utils.email_processors import email_processing


@app.task(name="task_email_processing")
def task_email_processing():
    email_processing()
