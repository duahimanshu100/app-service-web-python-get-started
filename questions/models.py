from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Questions(models.Model):
    questionId = models.CharField(db_column='questionId', primary_key=True, max_length=36)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    createdBy = models.TextField(db_column='createdBy', blank=True, null=True)  # Field name made lowercase.
    createdDate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.
    modifiedBy = models.TextField(db_column='modifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifiedDate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions'