# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accessmanagement(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=36)  # Field name made lowercase.
    pagename = models.CharField(db_column='PageName', max_length=100)  # Field name made lowercase.
    selectorunselect = models.BooleanField(db_column='SelectORUnselect')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccessManagement'


class Accountclinicassignment(models.Model):
    accountclinicid = models.CharField(db_column='AccountClinicId', primary_key=True, max_length=36)  # Field name made lowercase.
    accountid = models.ForeignKey('Accounts', models.DO_NOTHING, db_column='AccountId')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountClinicAssignment'


class Accountdocumentsecret(models.Model):
    accountdocumentsecretid = models.CharField(db_column='AccountDocumentSecretId', primary_key=True, max_length=36)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountId', max_length=36)  # Field name made lowercase.
    documentsecret = models.TextField(db_column='DocumentSecret')  # Field name made lowercase.
    ispasswordchanged = models.BooleanField(db_column='IsPasswordChanged')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountDocumentSecret'


class Accountroleassignment(models.Model):
    accountroleid = models.CharField(db_column='AccountRoleId', primary_key=True, max_length=36)  # Field name made lowercase.
    accountid = models.ForeignKey('Accounts', models.DO_NOTHING, db_column='AccountId')  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=36)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountRoleAssignment'


class Accounts(models.Model):
    accountid = models.CharField(db_column='accountId', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.TextField(db_column='userName', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.TextField(db_column='emailAddress', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(blank=True, null=True)
    securityquestion1 = models.TextField(db_column='securityQuestion1', blank=True, null=True)  # Field name made lowercase.
    securityquestionanswer1 = models.TextField(db_column='securityQuestionAnswer1', blank=True, null=True)  # Field name made lowercase.
    securityquestion2 = models.TextField(db_column='securityQuestion2', blank=True, null=True)  # Field name made lowercase.
    securityquestionanswer2 = models.TextField(db_column='securityQuestionAnswer2', blank=True, null=True)  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Accounts'


class Applicationusagestatistics(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    applicationname = models.TextField(db_column='ApplicationName')  # Field name made lowercase.
    usage = models.FloatField(db_column='Usage')  # Field name made lowercase.
    dataunit = models.TextField(db_column='DataUnit')  # Field name made lowercase.
    emaildate = models.DateTimeField(db_column='EmailDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicationUsageStatistics'


class Capturerate(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    captureratevalue = models.FloatField(db_column='CaptureRateValue')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CaptureRate'


class Categorycampaignconfiguration(models.Model):
    categorycampaignid = models.CharField(db_column='CategoryCampaignId', primary_key=True, max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    macaddress = models.TextField(db_column='MacAddress')  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    filename = models.TextField(db_column='FileName', blank=True, null=True)  # Field name made lowercase.
    timer = models.IntegerField(db_column='Timer')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoryCampaignConfiguration'


class Choices(models.Model):
    choiceid = models.CharField(db_column='choiceId', primary_key=True, max_length=36)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    questionid = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questionId')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Choices'


class Clinicaddtionalattributevalues(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=36)  # Field name made lowercase.
    fieldid = models.ForeignKey('Clinicaddtionalattributes', models.DO_NOTHING, db_column='FieldId')  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAddtionalAttributeValues'


class Clinicaddtionalattributes(models.Model):
    fieldid = models.CharField(db_column='FieldId', primary_key=True, max_length=36)  # Field name made lowercase.
    fieldname = models.TextField(db_column='FieldName')  # Field name made lowercase.
    fieldtype = models.IntegerField(db_column='FieldType')  # Field name made lowercase.
    clinicid = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAddtionalAttributes'


class Clinicaddtionalfieldsconfiguration(models.Model):
    fieldid = models.CharField(db_column='FieldId', primary_key=True, max_length=36)  # Field name made lowercase.
    fieldname = models.TextField(db_column='FieldName')  # Field name made lowercase.
    fieldtype = models.IntegerField(db_column='FieldType')  # Field name made lowercase.
    clinicid = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='Isdeleted')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    fieldtypedescription = models.TextField(db_column='FieldTypeDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAddtionalFieldsConfiguration'


class Clinicaddtionalfieldsconfigurationvalues(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=36)  # Field name made lowercase.
    fieldid = models.ForeignKey(Clinicaddtionalfieldsconfiguration, models.DO_NOTHING, db_column='FieldId')  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='Isdeleted')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAddtionalFieldsConfigurationValues'


class Clinicarchiverequests(models.Model):
    clinicarchiverequestsid = models.CharField(db_column='ClinicArchiveRequestsId', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    isanonymise_backup = models.BooleanField(db_column='IsAnonymise_Backup')  # Field name made lowercase.
    isarchive = models.BooleanField(db_column='IsArchive')  # Field name made lowercase.
    isarchive_delete = models.BooleanField(db_column='IsArchive_Delete')  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.
    process_start_datetime = models.DateTimeField(db_column='Process_Start_Datetime', blank=True, null=True)  # Field name made lowercase.
    process_end_datetime = models.DateTimeField(db_column='Process_End_Datetime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicArchiveRequests'


class Cliniccategories(models.Model):
    categoryid = models.CharField(db_column='CategoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    clinicid = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    questionid = models.ForeignKey('Questions', models.DO_NOTHING, db_column='QuestionId')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicCategories'


class Clinicdashboardsectionitems(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    sectionid = models.ForeignKey('Clinicdashboardsections', models.DO_NOTHING, db_column='SectionId')  # Field name made lowercase.
    widgetnames = models.TextField(db_column='WidgetNames')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicDashboardSectionItems'


class Clinicdashboardsections(models.Model):
    sectionid = models.CharField(db_column='SectionId', primary_key=True, max_length=36)  # Field name made lowercase.
    sectionname = models.CharField(db_column='SectionName', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicDashboardSections'


class Clinicfloormap(models.Model):
    clinicfloormapid = models.CharField(db_column='ClinicFloorMapId', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicFloorMap'


class Clinicfloormapcoordinates(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    areaid = models.CharField(db_column='AreaId', max_length=36)  # Field name made lowercase.
    clinicfloormapid = models.ForeignKey(Clinicfloormap, models.DO_NOTHING, db_column='ClinicFloorMapId')  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=100)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=150)  # Field name made lowercase.
    rectanglecoordinates = models.CharField(db_column='RectangleCoordinates', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicFloorMapCoordinates'


class Clinicgroupconfiguration(models.Model):
    groupid = models.CharField(db_column='GroupId', primary_key=True, max_length=36)  # Field name made lowercase.
    groupname = models.TextField(db_column='GroupName')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicGroupConfiguration'


class Clinicgroupconfigurationitems(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    groupid = models.ForeignKey(Clinicgroupconfiguration, models.DO_NOTHING, db_column='GroupId')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicGroupConfigurationItems'


class Cliniclogo(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey('Clinicmaintenance', models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicLogo'


class Clinicmaintenance(models.Model):
    clinicid = models.CharField(db_column='ClinicId', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicname = models.TextField(db_column='ClinicName')  # Field name made lowercase.
    clinicaddress = models.TextField(db_column='ClinicAddress')  # Field name made lowercase.
    landingpageurl = models.TextField(db_column='LandingPageUrl', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    shoppingurl = models.TextField(db_column='ShoppingUrl', blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=100)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicMaintenance'


class Clinicobservationconfiguration(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinicmaintenance, models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    roleid = models.ForeignKey('Clinicroles', models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    layoutid = models.ForeignKey('Dynamicdashboard', models.DO_NOTHING, db_column='LayoutId')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isdirectcomparsion = models.BooleanField(db_column='IsDirectComparsion', blank=True, null=True)  # Field name made lowercase.
    clinicidentifier = models.CharField(db_column='ClinicIdentifier', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicObservationConfiguration'


class Clinicobservationconfigurationitems(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    layoutid = models.ForeignKey('Dynamicdashboard', models.DO_NOTHING, db_column='LayoutId')  # Field name made lowercase.
    observationtext = models.CharField(db_column='ObservationText', max_length=300)  # Field name made lowercase.
    observationvariable = models.CharField(db_column='ObservationVariable', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    configurationid = models.CharField(db_column='ConfigurationId', max_length=36)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicObservationConfigurationItems'


class Clinicpolicyconfiguration(models.Model):
    policyid = models.CharField(db_column='PolicyId', primary_key=True, max_length=36)  # Field name made lowercase.
    policyname = models.TextField(db_column='PolicyName')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinicmaintenance, models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='Isdeleted')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicPolicyConfiguration'


class Clinicpolicyhistoryconfiguration(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    policyname = models.TextField(db_column='PolicyName')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    policyid = models.ForeignKey(Clinicpolicyconfiguration, models.DO_NOTHING, db_column='PolicyId')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='Isdeleted')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicPolicyHistoryConfiguration'


class Clinicrecommendations(models.Model):
    recommendationid = models.CharField(db_column='RecommendationId', primary_key=True, max_length=36)  # Field name made lowercase.
    videolink = models.TextField(db_column='VideoLink', blank=True, null=True)  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='VisitCount')  # Field name made lowercase.
    subcategoryid = models.ForeignKey('Clinicsubcategories', models.DO_NOTHING, db_column='SubCategoryId')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicRecommendations'


class Clinicrecommendationsfeedback(models.Model):
    feedbackid = models.CharField(db_column='FeedbackId', primary_key=True, max_length=36)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    videourl = models.TextField(db_column='VideoUrl')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicRecommendationsFeedback'


class Clinicrecommendationsusercomments(models.Model):
    commentid = models.CharField(db_column='CommentId', primary_key=True, max_length=36)  # Field name made lowercase.
    usercomment = models.CharField(db_column='UserComment', max_length=1000)  # Field name made lowercase.
    videourl = models.TextField(db_column='VideoUrl')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    subcategoryname = models.TextField(db_column='SubCategoryName')  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='VisitCount')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicRecommendationsUserComments'


class Clinicroles(models.Model):
    roleid = models.CharField(db_column='RoleId', primary_key=True, max_length=36)  # Field name made lowercase.
    rolename = models.TextField(db_column='RoleName')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicRoles'


class Clinicspecialevents(models.Model):
    specialeventid = models.CharField(db_column='SpecialEventId', primary_key=True, max_length=36)  # Field name made lowercase.
    specialeventdate = models.TextField(db_column='SpecialEventDate')  # Field name made lowercase.
    label = models.TextField(db_column='Label')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicSpecialEvents'


class Clinicsubcategories(models.Model):
    subcategoryid = models.CharField(db_column='SubCategoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    subcategoryname = models.TextField(db_column='SubCategoryName', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Cliniccategories, models.DO_NOTHING, db_column='CategoryId')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicSubCategories'


class Clinicsupportemailconfiguration(models.Model):
    departmentid = models.CharField(db_column='DepartmentId', primary_key=True, max_length=36)  # Field name made lowercase.
    departmentname = models.TextField(db_column='DepartmentName')  # Field name made lowercase.
    macaddress = models.TextField(db_column='MacAddress')  # Field name made lowercase.
    emailaddress = models.TextField(db_column='EmailAddress')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicSupportEmailConfiguration'


class Clinicuserrecommendations(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    recommendationtype = models.TextField(db_column='RecommendationType')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientipaddress = models.TextField(db_column='ClientIpAddress')  # Field name made lowercase.
    recommendationlink = models.TextField(db_column='RecommendationLink', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicUserRecommendations'


class Clinicuserselectedcategories(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=200)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicUserSelectedCategories'


class Clinicuserselectedsubcategories(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    subcategorydescription = models.TextField(db_column='SubCategoryDescription')  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=200)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicUserSelectedSubCategories'


class Clinicvisitedcategoriesrank(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription', blank=True, null=True)  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicVisitedCategoriesRank'


class Clinicvisitedoptions(models.Model):
    clinicvisitedoptionid = models.CharField(db_column='clinicVisitedOptionId', primary_key=True, max_length=36)  # Field name made lowercase.
    choiceid = models.ForeignKey(Choices, models.DO_NOTHING, db_column='choiceId')  # Field name made lowercase.
    choicedescription = models.TextField(db_column='choiceDescription', blank=True, null=True)  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='ssidMacAddress', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField()
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicVisitedOptions'


class Clinicvisitedsubcategoriesrank(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    subcategorydescription = models.TextField(db_column='SubCategoryDescription', blank=True, null=True)  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicVisitedSubCategoriesRank'


class Confirmation(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    confirmationdescription = models.TextField(db_column='ConfirmationDescription')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientipaddress = models.TextField(db_column='ClientIpAddress')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Confirmation'


class Customerclinicconfiguredfieldsdata(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=36)  # Field name made lowercase.
    fieldid = models.ForeignKey(Clinicaddtionalfieldsconfiguration, models.DO_NOTHING, db_column='FieldId')  # Field name made lowercase.
    customermacaddress = models.TextField(db_column='CustomerMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerClinicConfiguredFieldsData'


class Customersentemail(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentId', max_length=36)  # Field name made lowercase.
    departmentdescription = models.TextField(db_column='DepartmentDescription')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    emailcontent = models.TextField(db_column='EmailContent')  # Field name made lowercase.
    emailsentdate = models.DateTimeField(db_column='EmailSentDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerSentEmail'


class Customers(models.Model):
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=100)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', primary_key=True, max_length=100)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    countrycode = models.TextField(db_column='CountryCode')  # Field name made lowercase.
    issocialuser = models.BooleanField(db_column='isSocialUser')  # Field name made lowercase.
    isqrcode = models.BooleanField(db_column='isQrCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Customershistory(models.Model):
    customershistoryid = models.CharField(db_column='CustomersHistoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=100)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    countrycode = models.TextField(db_column='CountryCode')  # Field name made lowercase.
    issocialuser = models.BooleanField(db_column='isSocialUser')  # Field name made lowercase.
    isqrcode = models.BooleanField(db_column='isQrCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomersHistory'


class Dashboardfilterconfiguration(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=36)  # Field name made lowercase.
    layoutid = models.CharField(db_column='LayoutId', max_length=36)  # Field name made lowercase.
    year = models.BooleanField(db_column='Year')  # Field name made lowercase.
    quarter = models.BooleanField(db_column='Quarter')  # Field name made lowercase.
    monthly = models.BooleanField(db_column='Monthly')  # Field name made lowercase.
    weekly = models.BooleanField(db_column='Weekly')  # Field name made lowercase.
    specialevents = models.BooleanField(db_column='SpecialEvents')  # Field name made lowercase.
    customdateranges = models.BooleanField(db_column='CustomDateRanges')  # Field name made lowercase.
    additionalattributes = models.BooleanField(db_column='AdditionalAttributes')  # Field name made lowercase.
    clinicgroups = models.BooleanField(db_column='ClinicGroups')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DashboardFilterConfiguration'


class Dashboardlayouthtml(models.Model):
    sectionid = models.CharField(db_column='SectionId', max_length=36)  # Field name made lowercase.
    sectionname = models.CharField(db_column='SectionName', max_length=50)  # Field name made lowercase.
    layoutdesign = models.TextField(db_column='LayoutDesign')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    variableid = models.CharField(db_column='VariableId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    chartoptions = models.TextField(db_column='ChartOptions', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DashboardLayoutHtml'


class Dashboardthemeconfiguration(models.Model):
    themeid = models.CharField(db_column='ThemeId', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    themejson = models.CharField(db_column='ThemeJson', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DashboardThemeConfiguration'


class Dynamicdashboard(models.Model):
    dashboardid = models.CharField(db_column='DashboardId', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinicmaintenance, models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    roleid = models.ForeignKey(Clinicroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    dashboardlayout = models.TextField(db_column='DashBoardLayout')  # Field name made lowercase.
    layoutoptions = models.TextField(db_column='LayoutOptions')  # Field name made lowercase.
    dashboardtype = models.ForeignKey('Lookup', models.DO_NOTHING, db_column='DashboardType')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    layoutname = models.CharField(db_column='LayoutName', max_length=100)  # Field name made lowercase.
    isdirectcomparsion = models.BooleanField(db_column='IsDirectComparsion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DynamicDashboard'


class Engagement(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    dailyaverage_5_20_min = models.IntegerField(db_column='DailyAverage_5_20_Min')  # Field name made lowercase.
    dailyaverage_20_60_min = models.IntegerField(db_column='DailyAverage_20_60_Min')  # Field name made lowercase.
    dailyaverage_1_6_hrs = models.IntegerField(db_column='DailyAverage_1_6_hrs')  # Field name made lowercase.
    dailyaverage_6_plus_hrs = models.IntegerField(db_column='DailyAverage_6_Plus_hrs')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Engagement'


class Landingpagecampaignconfiguration(models.Model):
    landingpagecampaignid = models.CharField(db_column='LandingPageCampaignId', primary_key=True, max_length=36)  # Field name made lowercase.
    macaddress = models.TextField(db_column='MacAddress')  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    filename = models.TextField(db_column='FileName', blank=True, null=True)  # Field name made lowercase.
    timer = models.IntegerField(db_column='Timer')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LandingPageCampaignConfiguration'


class Lookup(models.Model):
    lookupid = models.AutoField(db_column='lookupId', primary_key=True)  # Field name made lowercase.
    lookupname = models.TextField(db_column='lookupName', blank=True, null=True)  # Field name made lowercase.
    lookuptype = models.TextField(db_column='lookupType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookUp'


class LookupLocalbackup(models.Model):
    lookupid = models.AutoField(db_column='lookupId')  # Field name made lowercase.
    lookupname = models.TextField(db_column='lookupName', blank=True, null=True)  # Field name made lowercase.
    lookuptype = models.TextField(db_column='lookupType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookUp_localbackup'


class Loyalty(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    firsttime = models.IntegerField(db_column='FirstTime')  # Field name made lowercase.
    daily = models.IntegerField(db_column='Daily')  # Field name made lowercase.
    weekly = models.IntegerField(db_column='Weekly')  # Field name made lowercase.
    occasional = models.IntegerField(db_column='Occasional')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Loyalty'


class Marketingmessage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientmacaddress = models.TextField(db_column='ClientMacAddress')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketingMessage'


class Medianvisitlength(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    visitlength = models.FloatField(db_column='VisitLength')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MedianVisitLength'


class Merakienvironment(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    environment = models.TextField(db_column='Environment')  # Field name made lowercase.
    macaddress = models.CharField(db_column='Macaddress', primary_key=True, max_length=450)  # Field name made lowercase.
    accesspointidentifier = models.TextField(db_column='AccessPointIdentifier', blank=True, null=True)  # Field name made lowercase.
    validatorkey = models.TextField(db_column='ValidatorKey', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MerakiEnvironment'


class Merakiusersessions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    sessionstart = models.DateTimeField(db_column='SessionStart')  # Field name made lowercase.
    sessionend = models.DateTimeField(db_column='SessionEnd')  # Field name made lowercase.
    sessiontimeinminutes = models.IntegerField(db_column='SessionTimeInMinutes')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MerakiUserSessions'


class Merakivalidator(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    validator = models.TextField(db_column='Validator')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Merakivalidator'


class Networkusagestatistics(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinicmaintenance, models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    totaldatatransferred = models.FloatField(db_column='TotalDataTransferred')  # Field name made lowercase.
    totaldatadownloaded = models.FloatField(db_column='TotalDataDownloaded')  # Field name made lowercase.
    totaldatauploaded = models.FloatField(db_column='TotalDataUploaded')  # Field name made lowercase.
    dataunit = models.TextField(db_column='DataUnit')  # Field name made lowercase.
    emaildate = models.DateTimeField(db_column='EmailDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NetworkUsageStatistics'


class Platformusers(models.Model):
    platformuserid = models.AutoField(db_column='PlatformUserId', primary_key=True)  # Field name made lowercase.
    ipv4address = models.CharField(db_column='Ipv4address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    unc = models.CharField(max_length=100, blank=True, null=True)
    seentime = models.DateTimeField(blank=True, null=True)
    ssid = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    clientmac = models.CharField(max_length=100, blank=True, null=True)
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seenepoch = models.CharField(db_column='seenEpoch', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rssi = models.CharField(max_length=100, blank=True, null=True)
    ipv6 = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlatformUsers'


class Platformusershistory(models.Model):
    platformuserhistoryid = models.AutoField(db_column='PlatformUserHistoryId', primary_key=True)  # Field name made lowercase.
    ipv4address = models.CharField(db_column='Ipv4address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    unc = models.CharField(max_length=100, blank=True, null=True)
    seentime = models.DateTimeField(blank=True, null=True)
    ssid = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    clientmac = models.CharField(max_length=100, blank=True, null=True)
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seenepoch = models.CharField(db_column='seenEpoch', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rssi = models.CharField(max_length=100, blank=True, null=True)
    ipv6 = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlatformUsersHistory'


class Proximity(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    connected = models.IntegerField(db_column='Connected')  # Field name made lowercase.
    visitors = models.IntegerField(db_column='Visitors')  # Field name made lowercase.
    passersby = models.IntegerField(db_column='PassersBy')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proximity'


class Questionnariechoice(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    choicedescription = models.TextField(db_column='ChoiceDescription')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientipaddress = models.TextField(db_column='ClientIpAddress')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionnarieChoice'


class Questions(models.Model):
    questionid = models.CharField(db_column='questionId', primary_key=True, max_length=36)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions'


class Recommendations(models.Model):
    recommendationid = models.CharField(db_column='recommendationId', primary_key=True, max_length=36)  # Field name made lowercase.
    websitelink = models.TextField(db_column='websiteLink', blank=True, null=True)  # Field name made lowercase.
    youtubelink = models.TextField(db_column='youtubeLink', blank=True, null=True)  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='visitCount')  # Field name made lowercase.
    choiceid = models.ForeignKey(Choices, models.DO_NOTHING, db_column='choiceId')  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recommendations'


class Repeatvisitorrate(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    visitorrate = models.IntegerField(db_column='VisitorRate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepeatVisitorRate'


class Ssids(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinicmaintenance, models.DO_NOTHING, db_column='ClinicId')  # Field name made lowercase.
    macaddress = models.TextField(db_column='Macaddress')  # Field name made lowercase.
    ssid = models.TextField(db_column='Ssid')  # Field name made lowercase.
    lanip = models.TextField(db_column='Lanip')  # Field name made lowercase.
    publicip = models.TextField(db_column='Publicip')  # Field name made lowercase.
    model = models.TextField(db_column='Model')  # Field name made lowercase.
    serialnumber = models.TextField(db_column='SerialNumber')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ssids'


class Subcategorycampaignconfiguration(models.Model):
    subcategorycampaignid = models.CharField(db_column='SubcategoryCampaignId', primary_key=True, max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubcategoryId', max_length=36)  # Field name made lowercase.
    macaddress = models.TextField(db_column='MacAddress')  # Field name made lowercase.
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    filename = models.TextField(db_column='FileName', blank=True, null=True)  # Field name made lowercase.
    timer = models.IntegerField(db_column='Timer')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubcategoryCampaignConfiguration'


class Userrecommendation(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    recommendationtype = models.TextField(db_column='RecommendationType')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientipaddress = models.TextField(db_column='ClientIpAddress')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    recommendationlink = models.TextField(db_column='RecommendationLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRecommendation'


class Venue(models.Model):
    venueid = models.CharField(db_column='VenueId', primary_key=True, max_length=36)  # Field name made lowercase.
    venuename = models.TextField(db_column='VenueName')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Venue'


class Venueholidaymanagement(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinicmaintenance, models.DO_NOTHING, db_column='ClinicId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    holidayname = models.CharField(db_column='HolidayName', max_length=150)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VenueHolidayManagement'


class Venuesocialmediaapplications(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    applicationname = models.TextField(db_column='ApplicationName')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    issocialmediaapp = models.BooleanField(db_column='IsSocialMediaApp')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VenueSocialMediaApplications'


class Venuessid(models.Model):
    key = models.CharField(db_column='Key', max_length=36)  # Field name made lowercase.
    venueid = models.ForeignKey(Venue, models.DO_NOTHING, db_column='VenueId')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', primary_key=True, max_length=450)  # Field name made lowercase.
    ssid = models.TextField(db_column='Ssid', blank=True, null=True)  # Field name made lowercase.
    lanipaddress = models.TextField(db_column='LanIpAddress', blank=True, null=True)  # Field name made lowercase.
    publicipaddress = models.TextField(db_column='PublicIpAddress', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.TextField(db_column='SerialNumber', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VenueSsid'


class Webappsintegration(models.Model):
    webappid = models.CharField(db_column='WebAppId', primary_key=True, max_length=36)  # Field name made lowercase.
    webappname = models.TextField(db_column='WebAppName')  # Field name made lowercase.
    redirectionurl = models.TextField(db_column='RedirectionUrl')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WebAppsIntegration'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class ApplicationusagestatisticsBackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    applicationname = models.TextField(db_column='ApplicationName')  # Field name made lowercase.
    usage = models.FloatField(db_column='Usage')  # Field name made lowercase.
    dataunit = models.TextField(db_column='DataUnit')  # Field name made lowercase.
    emaildate = models.DateTimeField(db_column='EmailDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicationUsageStatistics_backup'


class ApplicationusagestatisticsLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    applicationname = models.TextField(db_column='ApplicationName')  # Field name made lowercase.
    usage = models.FloatField(db_column='Usage')  # Field name made lowercase.
    dataunit = models.TextField(db_column='DataUnit')  # Field name made lowercase.
    emaildate = models.DateTimeField(db_column='EmailDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicationUsageStatistics_localbackup'


class CapturerateLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    captureratevalue = models.FloatField(db_column='CaptureRateValue')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'captureRate_localbackup'


class CapturerateBackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    captureratevalue = models.FloatField(db_column='CaptureRateValue')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'capturerate_backup'


class CliniccategoriesLocalbackup(models.Model):
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    questionid = models.CharField(db_column='QuestionId', max_length=36)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicCategories_localbackup'


class CliniclogoLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicLogo_localbackup'


class ClinicmaintenanceLocalbackup(models.Model):
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    clinicname = models.TextField(db_column='ClinicName')  # Field name made lowercase.
    clinicaddress = models.TextField(db_column='ClinicAddress')  # Field name made lowercase.
    landingpageurl = models.TextField(db_column='LandingPageUrl', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    shoppingurl = models.TextField(db_column='ShoppingUrl', blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=100)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicMaintenance_localbackup'


class ClinicrecommendationsfeedbacksLocalbackup(models.Model):
    feedbackid = models.CharField(db_column='FeedbackId', max_length=36)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    videourl = models.TextField(db_column='VideoUrl')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicRecommendationsFeedbacks_localbackup'


class ClinicrecommendationsusercommentsLocalbackup(models.Model):
    commentid = models.CharField(db_column='CommentId', max_length=36)  # Field name made lowercase.
    usercomment = models.CharField(db_column='UserComment', max_length=1000)  # Field name made lowercase.
    videourl = models.TextField(db_column='VideoUrl')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    subcategoryname = models.TextField(db_column='SubCategoryName')  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='VisitCount')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicRecommendationsUserComments_localbackup'


class ClinicrecommendationsLocalbackup(models.Model):
    recommendationid = models.CharField(db_column='RecommendationId', max_length=36)  # Field name made lowercase.
    videolink = models.TextField(db_column='VideoLink', blank=True, null=True)  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='VisitCount')  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicRecommendations_localbackup'


class ClinicspecialeventsLocalbackup(models.Model):
    specialeventid = models.CharField(db_column='SpecialEventId', max_length=36)  # Field name made lowercase.
    specialeventdate = models.TextField(db_column='SpecialEventDate')  # Field name made lowercase.
    label = models.TextField(db_column='Label')  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicSpecialEvents_localbackup'


class ClinicsubcategoriesLocalbackup(models.Model):
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    subcategoryname = models.TextField(db_column='SubCategoryName', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicSubCategories_localbackup'


class ClinicuserrecommendationsLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    recommendationtype = models.TextField(db_column='RecommendationType')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientipaddress = models.TextField(db_column='ClientIpAddress')  # Field name made lowercase.
    recommendationlink = models.TextField(db_column='RecommendationLink', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicUserRecommendations_localbackup'


class ClinicuserselectedcategoriesLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription')  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=200)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicUserSelectedCategories_localbackup'


class ClinicuserselectedsubcategoriesLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    subcategorydescription = models.TextField(db_column='SubCategoryDescription')  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=200)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=200)  # Field name made lowercase.
    clientipaddress = models.CharField(db_column='ClientIpAddress', max_length=200)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicUserSelectedSubCategories_localbackup'


class ClinicvisitedcategoriesrankLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='CategoryDescription', blank=True, null=True)  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicVisitedCategoriesRank_localbackup'


class ClinicvisitedsubcategoriesrankLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=36)  # Field name made lowercase.
    subcategoryid = models.CharField(db_column='SubCategoryId', max_length=36)  # Field name made lowercase.
    subcategorydescription = models.TextField(db_column='SubCategoryDescription', blank=True, null=True)  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicVisitedSubCategoriesRank_localbackup'


class ConfirmationLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    confirmationdescription = models.TextField(db_column='ConfirmationDescription')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientipaddress = models.TextField(db_column='ClientIpAddress')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confirmation_localbackup'


class CustomersentemailLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentId', max_length=36)  # Field name made lowercase.
    departmentdescription = models.TextField(db_column='DepartmentDescription')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    emailcontent = models.TextField(db_column='EmailContent')  # Field name made lowercase.
    emailsentdate = models.DateTimeField(db_column='EmailSentDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customerSentEmail_localbackup'


class CustomershistoryLocalbackup(models.Model):
    customershistoryid = models.CharField(db_column='CustomersHistoryId', max_length=36)  # Field name made lowercase.
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=100)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    countrycode = models.TextField(db_column='CountryCode')  # Field name made lowercase.
    issocialuser = models.BooleanField(db_column='isSocialUser')  # Field name made lowercase.
    isqrcode = models.BooleanField(db_column='isQrCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customersHistory_localbackup'


class CustomersBackup(models.Model):
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=100)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    countrycode = models.TextField(db_column='CountryCode')  # Field name made lowercase.
    issocialuser = models.BooleanField(db_column='isSocialUser')  # Field name made lowercase.
    isqrcode = models.BooleanField(db_column='isQrCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers_backup'


class CustomersLocalbackup(models.Model):
    usermacaddress = models.CharField(db_column='UserMacAddress', max_length=100)  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=100)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    countrycode = models.TextField(db_column='CountryCode')  # Field name made lowercase.
    issocialuser = models.BooleanField(db_column='isSocialUser')  # Field name made lowercase.
    isqrcode = models.BooleanField(db_column='isQrCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers_localbackup'


class DynamicdashboardBackup(models.Model):
    dashboardid = models.CharField(db_column='DashboardId', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=36)  # Field name made lowercase.
    dashboardlayout = models.TextField(db_column='DashBoardLayout')  # Field name made lowercase.
    layoutoptions = models.TextField(db_column='LayoutOptions')  # Field name made lowercase.
    dashboardtype = models.IntegerField(db_column='DashboardType')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    layoutname = models.CharField(db_column='LayoutName', max_length=100)  # Field name made lowercase.
    isdirectcomparsion = models.BooleanField(db_column='IsDirectComparsion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dynamicdashboard_backup'


class EngagementLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    dailyaverage_5_20_min = models.IntegerField(db_column='DailyAverage_5_20_Min')  # Field name made lowercase.
    dailyaverage_20_60_min = models.IntegerField(db_column='DailyAverage_20_60_Min')  # Field name made lowercase.
    dailyaverage_1_6_hrs = models.IntegerField(db_column='DailyAverage_1_6_hrs')  # Field name made lowercase.
    dailyaverage_6_plus_hrs = models.IntegerField(db_column='DailyAverage_6_Plus_hrs')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'engagement_localbackup'


class LoyaltyLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    firsttime = models.IntegerField(db_column='FirstTime')  # Field name made lowercase.
    daily = models.IntegerField(db_column='Daily')  # Field name made lowercase.
    weekly = models.IntegerField(db_column='Weekly')  # Field name made lowercase.
    occasional = models.IntegerField(db_column='Occasional')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loyalty_localbackup'


class MarketingmessageLocalbackup(models.Model):
    id = models.AutoField(db_column='Id')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    clientmacaddress = models.TextField(db_column='ClientMacAddress')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marketingMessage_localbackup'


class MedianvisitlengthLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    visitlength = models.FloatField(db_column='VisitLength')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medianVisitLength_localbackup'


class MerakienvironmentLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    environment = models.TextField(db_column='Environment')  # Field name made lowercase.
    macaddress = models.CharField(db_column='Macaddress', max_length=450)  # Field name made lowercase.
    accesspointidentifier = models.TextField(db_column='AccessPointIdentifier', blank=True, null=True)  # Field name made lowercase.
    validatorkey = models.TextField(db_column='ValidatorKey', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merakiEnvironment_localbackup'


class MerakiusersessionsLocalbackup(models.Model):
    id = models.AutoField(db_column='Id')  # Field name made lowercase.
    usermacaddress = models.TextField(db_column='UserMacAddress')  # Field name made lowercase.
    ssidmacaddress = models.TextField(db_column='SsidMacAddress')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    sessionstart = models.DateTimeField(db_column='SessionStart')  # Field name made lowercase.
    sessionend = models.DateTimeField(db_column='SessionEnd')  # Field name made lowercase.
    sessiontimeinminutes = models.IntegerField(db_column='SessionTimeInMinutes')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merakiUserSessions_localbackup'


class MerakivalidatorLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    validator = models.TextField(db_column='Validator')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merakivalidator_localbackup'


class NetworkusagestatisticsLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    totaldatatransferred = models.FloatField(db_column='TotalDataTransferred')  # Field name made lowercase.
    totaldatadownloaded = models.FloatField(db_column='TotalDataDownloaded')  # Field name made lowercase.
    totaldatauploaded = models.FloatField(db_column='TotalDataUploaded')  # Field name made lowercase.
    dataunit = models.TextField(db_column='DataUnit')  # Field name made lowercase.
    emaildate = models.DateTimeField(db_column='EmailDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'networkUsageStatistics_localbackup'


class PlatformusershistoryLocalbackup(models.Model):
    platformuserhistoryid = models.AutoField(db_column='PlatformUserHistoryId')  # Field name made lowercase.
    ipv4address = models.CharField(db_column='Ipv4address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    unc = models.CharField(max_length=100, blank=True, null=True)
    seentime = models.DateTimeField(blank=True, null=True)
    ssid = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    clientmac = models.CharField(max_length=100, blank=True, null=True)
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seenepoch = models.CharField(db_column='seenEpoch', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rssi = models.CharField(max_length=100, blank=True, null=True)
    ipv6 = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platformUsersHistory_localbackup'


class PlatformusersLocalbackup(models.Model):
    platformuserid = models.AutoField(db_column='PlatformUserId')  # Field name made lowercase.
    ipv4address = models.CharField(db_column='Ipv4address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    unc = models.CharField(max_length=100, blank=True, null=True)
    seentime = models.DateTimeField(blank=True, null=True)
    ssid = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    clientmac = models.CharField(max_length=100, blank=True, null=True)
    ssidmacaddress = models.CharField(db_column='SsidMacAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    seenepoch = models.CharField(db_column='seenEpoch', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rssi = models.CharField(max_length=100, blank=True, null=True)
    ipv6 = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platformUsers_localbackup'


class ProximityBackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    connected = models.IntegerField(db_column='Connected')  # Field name made lowercase.
    visitors = models.IntegerField(db_column='Visitors')  # Field name made lowercase.
    passersby = models.IntegerField(db_column='PassersBy')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proximity_backup'


class ProximityLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    connected = models.IntegerField(db_column='Connected')  # Field name made lowercase.
    visitors = models.IntegerField(db_column='Visitors')  # Field name made lowercase.
    passersby = models.IntegerField(db_column='PassersBy')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proximity_localbackup'


class QuestionsLocalbackup(models.Model):
    questionid = models.CharField(db_column='questionId', max_length=36)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questions_localbackup'


class RecommendationsLocalbackup(models.Model):
    recommendationid = models.CharField(db_column='recommendationId', max_length=36)  # Field name made lowercase.
    websitelink = models.TextField(db_column='websiteLink', blank=True, null=True)  # Field name made lowercase.
    youtubelink = models.TextField(db_column='youtubeLink', blank=True, null=True)  # Field name made lowercase.
    visitcount = models.IntegerField(db_column='visitCount')  # Field name made lowercase.
    choiceid = models.CharField(db_column='choiceId', max_length=36)  # Field name made lowercase.
    createdby = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recommendations_localbackup'


class RepeatvisitorrateLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    network = models.TextField(db_column='Network', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    visitorrate = models.IntegerField(db_column='VisitorRate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    ssidmacaddress = models.CharField(db_column='SsidMacaddress', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repeatVisitorRate_localbackup'


class SsidsLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    macaddress = models.TextField(db_column='Macaddress')  # Field name made lowercase.
    ssid = models.TextField(db_column='Ssid')  # Field name made lowercase.
    lanip = models.TextField(db_column='Lanip')  # Field name made lowercase.
    publicip = models.TextField(db_column='Publicip')  # Field name made lowercase.
    model = models.TextField(db_column='Model')  # Field name made lowercase.
    serialnumber = models.TextField(db_column='SerialNumber')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ssids_localbackup'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class VenuesocialmediaapplicationsLocalbackup(models.Model):
    id = models.CharField(db_column='Id', max_length=36)  # Field name made lowercase.
    applicationname = models.TextField(db_column='ApplicationName')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    issocialmediaapp = models.BooleanField(db_column='IsSocialMediaApp')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venueSocialMediaApplications_localbackup'


class VenuessidLocalbackup(models.Model):
    key = models.CharField(db_column='Key', max_length=36)  # Field name made lowercase.
    venueid = models.CharField(db_column='VenueId', max_length=36)  # Field name made lowercase.
    clinicid = models.CharField(db_column='ClinicId', max_length=36)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MacAddress', max_length=450)  # Field name made lowercase.
    ssid = models.TextField(db_column='Ssid', blank=True, null=True)  # Field name made lowercase.
    lanipaddress = models.TextField(db_column='LanIpAddress', blank=True, null=True)  # Field name made lowercase.
    publicipaddress = models.TextField(db_column='PublicIpAddress', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.TextField(db_column='SerialNumber', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venueSsid_localbackup'


class WebappsintegrationLocalbackup(models.Model):
    webappid = models.CharField(db_column='WebAppId', max_length=36)  # Field name made lowercase.
    webappname = models.TextField(db_column='WebAppName')  # Field name made lowercase.
    redirectionurl = models.TextField(db_column='RedirectionUrl')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'webappsIntegration_localbackup'
