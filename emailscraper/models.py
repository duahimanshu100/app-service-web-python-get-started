import uuid
from django.db import models


class ClinicMaintenance(models.Model):
    clinic_id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False,
                                db_column="ClinicId")
    clinic_name = models.TextField(db_column="ClinicName")  # Field name made lowercase.
    clinic_address = models.TextField(
        db_column="ClinicAddress"
    )  # Field name made lowercase.
    landing_pageurl = models.TextField(
        db_column="LandingPageUrl", blank=True, null=True
    )  # Field name made lowercase.
    created_by = models.CharField(
        db_column="CreatedBy", max_length=100
    )  # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column="CreatedDate"
    )  # Field name made lowercase.
    modified_by = models.CharField(
        db_column="ModifiedBy", max_length=100
    )  # Field name made lowercase.
    modified_date = models.DateTimeField(
        db_column="ModifiedDate"
    )  # Field name made lowercase.
    shoppingurl = models.TextField(
        db_column="ShoppingUrl", blank=True, null=True
    )  # Field name made lowercase.
    latitude = models.CharField(
        db_column="Latitude", max_length=100
    )  # Field name made lowercase.
    longitude = models.CharField(
        db_column="Longitude", max_length=100
    )  # Field name made lowercase.

    class Meta:
        db_table = "ClinicMaintenance"
        managed = False


class NetworkUsageStatistics(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False,
        db_column="Id"
    )  # Field name made lowercase.
    clinic_id = models.ForeignKey(
        ClinicMaintenance, models.DO_NOTHING, db_column="ClinicId"
    )  # Field name made lowercase.
    total_data_transferred = models.FloatField(
        db_column="TotalDataTransferred"
    )  # Field name made lowercase.
    total_data_downloaded = models.FloatField(
        db_column="TotalDataDownloaded"
    )  # Field name made lowercase.
    total_data_uploaded = models.FloatField(
        db_column="TotalDataUploaded"
    )  # Field name made lowercase.
    data_unit = models.TextField(db_column="DataUnit")  # Field name made lowercase.
    email_date = models.DateTimeField(
        db_column="EmailDate"
    )  # Field name made lowercase.
    created_by = models.CharField(
        db_column="CreatedBy", max_length=100
    )  # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column="CreatedDate"
    )  # Field name made lowercase.
    modified_by = models.CharField(
        db_column="ModifiedBy", max_length=100
    )  # Field name made lowercase.
    modified_date = models.DateTimeField(
        db_column="ModifiedDate"
    )  # Field name made lowercase.
    ssid_mac_address = models.CharField(
        db_column="SsidMacAddress", max_length=450
    )  # Field name made lowercase.

    def __str__(self):
        return f"id: {self.id}, TotalDataTransferred : {self.total_data_transferred}"

    class Meta:
        db_table = "NetworkUsageStatistics"
        managed = False


class ApplicationUsageStatistics(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False,
        db_column="Id",
    )  # Field name made lowercase.
    clinic_id = models.ForeignKey(
        "ClinicMaintenance", models.DO_NOTHING, db_column="ClinicId"
    )  # Field name made lowercase.
    application_name = models.TextField(
        db_column="ApplicationName"
    )  # Field name made lowercase.
    usage = models.FloatField(db_column="Usage")  # Field name made lowercase.
    data_unit = models.TextField(db_column="DataUnit")  # Field name made lowercase.
    email_date = models.DateTimeField(
        db_column="EmailDate"
    )  # Field name made lowercase.
    created_by = models.CharField(
        db_column="CreatedBy", max_length=100
    )  # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column="CreatedDate"
    )  # Field name made lowercase.
    modified_by = models.CharField(
        db_column="ModifiedBy", max_length=100
    )  # Field name made lowercase.
    modified_date = models.DateTimeField(
        db_column="ModifiedDate"
    )  # Field name made lowercase.
    ssid_mac_address = models.CharField(
        db_column="SsidMacAddress", max_length=450
    )  # Field name made lowercase.

    class Meta:
        db_table = "ApplicationUsageStatistics"
        managed = False


class VenueSocialMediaApplications(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False,
        db_column="Id", 
    )  # Field name made lowercase.
    application_name = models.TextField(
        db_column="ApplicationName"
    )  # Field name made lowercase.
    is_active = models.BooleanField(db_column="IsActive")  # Field name made lowercase.
    is_socialmedia_app = models.BooleanField(
        db_column="IsSocialMediaApp"
    )  # Field name made lowercase.
    created_by = models.CharField(
        db_column="CreatedBy", max_length=100
    )  # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column="CreatedDate"
    )  # Field name made lowercase.
    modified_by = models.CharField(
        db_column="ModifiedBy", max_length=100
    )  # Field name made lowercase.
    modified_date = models.DateTimeField(
        db_column="ModifiedDate"
    )  # Field name made lowercase.

    class Meta:
        db_table = "VenueSocialMediaApplications"
        managed = False

class Ssids(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36,
        db_column="Id",
    )  # Field name made lowercase.
    clinic_id = models.ForeignKey(
        ClinicMaintenance, models.DO_NOTHING, db_column="ClinicId"
    )  # Field name made lowercase.
    mac_address = models.TextField(db_column="Macaddress")  # Field name made lowercase.
    ssid = models.TextField(db_column="Ssid")  # Field name made lowercase.
    lan_ip = models.TextField(db_column="Lanip")  # Field name made lowercase.
    public_ip = models.TextField(db_column="Publicip")  # Field name made lowercase.
    model = models.TextField(db_column="Model")  # Field name made lowercase.
    serial_number = models.TextField(
        db_column="SerialNumber"
    )  # Field name made lowercase.
    created_by = models.CharField(
        db_column="CreatedBy", max_length=100
    )  # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column="CreatedDate"
    )  # Field name made lowercase.
    modified_by = models.CharField(
        db_column="ModifiedBy", max_length=100
    )  # Field name made lowercase.
    modified_date = models.DateTimeField(
        db_column="ModifiedDate"
    )  # Field name made lowercase.

    class Meta:
        db_table = "Ssids"
        managed = False
