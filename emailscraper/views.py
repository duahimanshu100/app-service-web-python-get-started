from django.http import HttpResponse
from emailscraper.tasks import add


# Create your views here.
def celery_test(request):
    # TODO : Remove this celery test view,
    # this is only to test monitoring system
    for i in range(1, 100):
        add.delay(i, i * i)
    return HttpResponse("task done")
