from rest_framework import serializers

from clinics.models import ClinicMaintenance, ClinicAddtionalAttributes, ClinicAddtionalAttributeValues, \
    ClinicCategories, ClinicLogo, ClinicRecommendations


class ClinicMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicMaintenance
        fields = "__all__"
        # fields = ["id", "description", "created_by", "modified_by"]


class ClinicAddtionalAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAddtionalAttributes
        fields = "__all__"


class ClinicAddtionalAttributeValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAddtionalAttributeValues
        fields = "__all__"


class ClinicCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicCategories
        fields = "__all__"


class ClinicLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicLogo
        fields = "__all__"


class ClinicRecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicRecommendations
        fields = "__all__"
