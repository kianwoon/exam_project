from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
from subscription.models import Subscription
from classes.models import Classes


# Create your models here.
class UserSubscription(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    username = models.ForeignKey(User, on_delete=models.CASCADE, db_column='username', to_field='username')
    subscription_date = models.DateTimeField(blank=True, null=True)
    subscription_end = models.DateTimeField(blank=True, null=True)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE, db_column='subscription_id', to_field='subscription_id')
    # class_id = models.CharField(max_length=100) 
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE,db_column='class_id', to_field='class_id')

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '%s %s %s' % (self.username, self.subscription_date, self.subscription_end)
        

    class Meta:
        db_table = 'user_subscription'