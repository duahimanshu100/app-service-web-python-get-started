import uuid

from django.db import models

# Create your models here.
from questions.models import Questions


class ClinicMaintenance(models.Model):
    ClinicId = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36, editable=False,
                                db_column="ClinicId")
    # Field name made lowercase.
    ClinicName = models.TextField(db_column="ClinicName")  # Field name made lowercase.
    ClinicAddress = models.TextField(
        db_column="ClinicAddress"
    )  # Field name made lowercase.
    LandingPageUrl = models.TextField(
        db_column="LandingPageUrl", blank=True, null=True
    )  # Field name made lowercase.
    CreatedBy = models.CharField(
        db_column="CreatedBy", max_length=100
    )  # Field name made lowercase.
    CreatedDate = models.DateTimeField(
        db_column="CreatedDate"
    )  # Field name made lowercase.
    ModifiedBy = models.CharField(
        db_column="ModifiedBy", max_length=100
    )  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(
        db_column="ModifiedDate"
    )  # Field name made lowercase.
    ShoppingUrl = models.TextField(
        db_column="ShoppingUrl", blank=True, null=True
    )  # Field name made lowercase.
    Latitude = models.CharField(
        db_column="Latitude", max_length=100
    )  # Field name made lowercase.
    Longitude = models.CharField(
        db_column="Longitude", max_length=100
    )  # Field name made lowercase.

    class Meta:
        db_table = "ClinicMaintenance"
        managed = False


class ClinicAddtionalAttributes(models.Model):
    FieldId = models.CharField(db_column='FieldId', primary_key=True, max_length=36)  # Field name made lowercase.
    FieldName = models.TextField(db_column='FieldName')  # Field name made lowercase.
    FieldType = models.IntegerField(db_column='FieldType')  # Field name made lowercase.
    ClinicId = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING,
                                 db_column='ClinicId')  # Field name made lowercase.
    CreatedBy = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    CreatedDate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    ModifiedBy = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAddtionalAttributes'


class ClinicCategories(models.Model):
    CategoryId = models.CharField(db_column='CategoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    CategoryDescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    ClinicId = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING,
                                 db_column='ClinicId')  # Field name made lowercase.
    QuestionId = models.ForeignKey(Questions, models.DO_NOTHING, db_column='QuestionId')  # Field name made lowercase.
    CreatedBy = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    CreatedDate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    ModifiedBy = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicCategories'


class ClinicSubCategories(models.Model):
    SubCategoryId = models.CharField(db_column='SubCategoryId', primary_key=True,
                                     max_length=36)  # Field name made lowercase.
    SubCategoryName = models.TextField(db_column='SubCategoryName', blank=True, null=True)  # Field name made lowercase.
    CategoryId = models.ForeignKey(ClinicCategories, models.DO_NOTHING,
                                   db_column='CategoryId')  # Field name made lowercase.
    ClinicId = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    CreatedBy = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    CreatedDate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    ModifiedBy = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicSubCategories'


class ClinicRecommendations(models.Model):
    RecommendationId = models.CharField(db_column='RecommendationId', primary_key=True,
                                        max_length=36)  # Field name made lowercase.
    VideoLink = models.TextField(db_column='VideoLink', blank=True, null=True)  # Field name made lowercase.
    VisitCount = models.IntegerField(db_column='VisitCount')  # Field name made lowercase.
    SubCategoryId = models.ForeignKey('ClinicSubCategories', models.DO_NOTHING,
                                      db_column='SubCategoryId')  # Field name made lowercase.
    CreatedBy = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    CreatedDate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    ModifiedBy = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicRecommendations'


class ClinicAddtionalAttributeValues(models.Model):
    Key = models.CharField(db_column='Key', primary_key=True, max_length=36)  # Field name made lowercase.
    FieldId = models.ForeignKey('ClinicAddtionalAttributes', models.DO_NOTHING,
                                db_column='FieldId')  # Field name made lowercase.
    Value = models.TextField(db_column='Value')  # Field name made lowercase.
    CreatedBy = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    CreatedDate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    ModifiedBy = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    SsidMacAddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAddtionalAttributeValues'


class ClinicLogo(models.Model):
    Id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    ClinicId = models.ForeignKey('ClinicMaintenance', models.DO_NOTHING,
                                 db_column='ClinicId')  # Field name made lowercase.
    Image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    Filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    CreatedBy = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    CreatedDate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    ModifiedBy = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    ModifiedDate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicLogo'
