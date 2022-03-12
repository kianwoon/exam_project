--------------
/media/sf_dev/exam_project/src/exam_project
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Subscription(models.Model):
    subscription_id = models.CharField(primary_key=True, max_length=45)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    rebate = models.DecimalField(max_digits=10, decimal_places=0)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription'
