from django.db import models
from django.contrib.auth.models import User
from topics.models import Topics 
import uuid
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class ExercisePaper(models.Model):
    default_style=0
    style_choice = [
        (default_style, 'Working in progress'),
        (1, 'Completed')
    ]

    exercise_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='username') 
    exercise_date = models.DateTimeField(auto_now=True)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE, db_column='topic_id', to_field='topic_id')
    status = models.IntegerField(choices=style_choice, default=default_style, db_column="status") 
    result = models.DecimalField(max_digits=10,decimal_places=2, default=0, db_column='result')

    class Meta:
        managed = False
        db_table = 'exercise_paper'

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '%s %s %s' % (self.exercise_id, self.user_id, self.exercise_date)

    def get_absolute_url(self):
        return reverse('exercise:loading_questions', kwargs={'id':self.exercise_id})
  