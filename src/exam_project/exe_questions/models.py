from django.db import models
from exercise.models import ExercisePaper
from questions_bank.models import QuestionsBank
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.


class ExerciseQuestions(models.Model):
    
    exercise_id= models.ForeignKey(ExercisePaper, on_delete=models.CASCADE, db_column='exercise_id', to_field='exercise_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='username')     
    question_id = models.ForeignKey(QuestionsBank, on_delete=models.CASCADE, db_column='question_id', to_field='question_id')


    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.topic_id}, {self.topic_name}, {self.class_id}'
        return '%s - %s - %s' % (self.exercise_id, self.user_id, self.question_id)
 
    def get_absolute_url(self):
        return reverse('exe_questions:display_specific_ques', kwargs={'id':self.question_id.question_id})


    class Meta:
        managed = False
        db_table = 'exercise_questions'

