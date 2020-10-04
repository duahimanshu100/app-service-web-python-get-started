from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from questions.api.v2.views import QuestionViewSet

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)
urlpatterns = router.urls
