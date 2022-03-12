from django.db import models
from questions_bank.models import QuestionsBank
from django.contrib.auth.models import User
from answers_bank.models import AnswersBank
from exercise.models import ExercisePaper


# Create your models here.
class ExerciseAnswers(models.Model):
    question_id = models.ForeignKey(QuestionsBank , on_delete=models.CASCADE, db_column='question_id', to_field='question_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', to_field='username')
    answer_id = models.ForeignKey(AnswersBank, on_delete=models.CASCADE, db_column='answer_id', to_field='answer_id')
    answer_for_opentext = models.TextField(db_column='answer_for_opentext')
    exercise_id = models.ForeignKey(ExercisePaper, on_delete=models.CASCADE, db_column='exercise_id', to_field='exercise_id')
    flag = models.IntegerField(default=0)
    class Meta:
        managed = False
        db_table = 'exercise_answers'

# exercise_id= models.ForeignKey(ExercisePaper, on_delete=models.CASCADE, db_column='exercise_id', to_field='exercise_id')

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.topic_id}, {self.topic_name}, {self.class_id}'
        return '%s - %s - %s - %s' % (self.question_id, self.user_id, self.answer_id, self.exercise_id)