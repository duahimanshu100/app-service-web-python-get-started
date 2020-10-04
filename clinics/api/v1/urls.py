from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from clinics.api.v1.views import ClinicMaintenanceViewSet, ClinicAddtionalAttributesViewSet, \
    ClinicAddtionalAttributeValuesViewSet, ClinicCategoriesViewSet, ClinicLogoViewSet, ClinicRecommendationsViewSet

router = DefaultRouter()
router.register(r"Clinic", ClinicMaintenanceViewSet)
router.register(r"ClinicAddtionalAttributes", ClinicAddtionalAttributesViewSet)
router.register(r"ClinicAddtionalAttributeValues", ClinicAddtionalAttributeValuesViewSet)
router.register(r"ClinicCategories", ClinicCategoriesViewSet)
router.register(r"ClinicLogo", ClinicLogoViewSet)
router.register(r"ClinicRecommendations", ClinicRecommendationsViewSet)
urlpatterns = router.urls
