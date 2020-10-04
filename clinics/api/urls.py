# urls.py
from django.urls import re_path, include

urlpatterns = [
    re_path(r"", include(("clinics.api.v1.urls", "v1"), namespace="v1")),
]
