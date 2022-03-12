from django.db import models
import uuid 
from uuid import uuid4

# Create your models here.
class Subscription(models.Model):
    subscription_id = models.UUIDField(default=uuid.uuid4, primary_key=True, max_length=45)
    title = models.CharField(max_length=200, db_column="title")
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    subscribe_value = models.IntegerField()
    rebate = models.DecimalField(max_digits=10, decimal_places=0)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '%s %s' % (self.title, self.desc)

    class Meta:
        managed = False
        db_table = 'subscription'