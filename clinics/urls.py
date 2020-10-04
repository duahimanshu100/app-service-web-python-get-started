from django.urls import path, include

urlpatterns = [
    path("api/", include("clinics.api.urls")),
]
