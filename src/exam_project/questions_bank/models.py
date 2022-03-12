from django.db import models
import uuid
from sch.models import Schools
from topics.models import Topics

# Create your models here.
class QuestionsBank(models.Model):
    default_style='1'
    style_choice = [
        (default_style, 'Multiple choices answer'),
        ('0', 'blank answer box')
    ]

    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    question_desc = models.TextField()
    tags = models.CharField(max_length=45)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE, db_column='topic_id')
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE, db_column='school_id')
    weightage = models.DecimalField(max_digits=10, decimal_places=0)
    styles = models.CharField(max_length=10, choices=style_choice, default=default_style)
    ref_image = models.ImageField(upload_to='ref_image')


    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '(%s) %s' % (self.topic_id, self.question_desc)

    class Meta:
        managed = False
        db_table = 'questions_bank'
