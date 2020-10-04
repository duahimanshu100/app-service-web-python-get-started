from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cis.settings")
app = Celery("cis")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


from celery.schedules import crontab

app.conf.timezone = "UTC"

app.conf.beat_schedule = {
    "task_email_processing": {
        "task": "task_email_processing",
        "schedule": crontab(hour=2),
    },
}
