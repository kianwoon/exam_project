from django.db import models
import uuid
from questions_bank.models import QuestionsBank

# Create your models here.
class AnswersBank(models.Model):
    default_style=0
    style_choice = [
        (default_style, 'Wrong answer'),
        (1, 'Correct answer ')
    ]

    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    question_id = models.ForeignKey(QuestionsBank,on_delete=models.CASCADE, db_column='question_id')
    answer_desc = models.TextField()
    flag = models.IntegerField(choices=style_choice, default=default_style)

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '%s' % (self.answer_desc)


    class Meta:
        managed = False
        db_table = 'answers_bank'
#        unique_together = (('answer_id', 'question_id'),)