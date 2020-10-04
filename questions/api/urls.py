# urls.py
from django.urls import re_path, include

urlpatterns = [
    re_path(r"^v1/", include(("questions.api.v1.urls", "v1"), namespace="v1")),
    re_path(r"^v2/", include(("questions.api.v2.urls", "v2"), namespace="v2")),
]
