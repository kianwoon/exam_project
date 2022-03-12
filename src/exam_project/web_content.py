# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WebContent(models.Model):
    id = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    style = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    links = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_content'
