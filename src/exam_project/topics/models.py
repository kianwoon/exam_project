from django.db import models
import uuid
from classes.models import Classes
from django.urls import reverse


# Create your models here.

class Topics(models.Model):
    default_status=0
    status_choice = [
        (default_status, 'OFF'),
        (1, 'LIVE')
    ]

    topic_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    topic_name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, to_field='class_id')
    desc = models.TextField(max_length=200)
    status = models.IntegerField(choices=status_choice, default=default_status)
    #class_name = models.ForeignKey(Classes, related_name='thing_id', to_field='class_id', on_delete=models.CASCADE)  # Field renamed because it was a Python reserved word.

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.topic_id}, {self.topic_name}, {self.class_id}'
        return '(%s) %s' % (self.class_id, self.topic_name)
 
    def get_absolute_url(self):

        return reverse('exercise:start_exercise', kwargs={'id':self.topic_id})

    class Meta:
        db_table = 'topics'
