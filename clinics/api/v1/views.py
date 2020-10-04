from rest_framework import viewsets

from cis.api_mixins import CisListModelMixin, CisRetrieveModelMixin, CisCreateModelMixin
from cis.api_viewsets import CisModelViewSet
from clinics.api.v1.serializers import ClinicMaintenanceSerializer, ClinicAddtionalAttributesSerializer, \
    ClinicAddtionalAttributeValuesSerializer, ClinicCategoriesSerializer, ClinicLogoSerializer, \
    ClinicRecommendationsSerializer
from clinics.models import ClinicMaintenance, ClinicAddtionalAttributes, ClinicAddtionalAttributeValues, \
    ClinicCategories, ClinicLogo, ClinicRecommendations

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class ClinicMaintenanceViewSet(CisModelViewSet):
    """
    A viewset for viewing and editing Clinic instances.
    """

    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = "ClinicId"
    serializer_class = ClinicMaintenanceSerializer
    queryset = ClinicMaintenance.objects.all()


class ClinicAddtionalAttributesViewSet(CisModelViewSet):
    """
    A viewset for viewing and editing Clinic instances.
    """

    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = "FieldId"
    serializer_class = ClinicAddtionalAttributesSerializer
    queryset = ClinicAddtionalAttributes.objects.all()


class ClinicAddtionalAttributeValuesViewSet(CisModelViewSet):
    """
    A viewset for viewing and editing Clinic instances.
    """

    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = "Key"
    serializer_class = ClinicAddtionalAttributeValuesSerializer
    queryset = ClinicAddtionalAttributeValues.objects.all()


class ClinicCategoriesViewSet(CisModelViewSet):
    """
    A viewset for viewing and editing Clinic instances.
    """

    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = "CategoryId"
    serializer_class = ClinicCategoriesSerializer
    queryset = ClinicCategories.objects.all()


class ClinicLogoViewSet(CisModelViewSet):
    """
    A viewset for viewing and editing Clinic instances.
    """

    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = "Id"
    serializer_class = ClinicLogoSerializer
    queryset = ClinicLogo.objects.all()


class ClinicRecommendationsViewSet(CisModelViewSet):
    """
    A viewset for viewing and editing Clinic instances.
    """

    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = "RecommendationId"
    serializer_class = ClinicRecommendationsSerializer
    queryset = ClinicRecommendations.objects.all()
