from django.db import models
from sch.models import Schools
from classes.models import Classes
from topics.models import Topics

# Create your models here.
def exam_paper_path(instances, filename):
    path = filename.split('.')[0]
    return '{0}/{1}'.format(path, filename)

class Ingestion(models.Model):
    default_status=0
    status_choice = [
        (default_status, 'OFF'),
        (1, 'LIVE')
    ]
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE, db_column='school_id', null=True, blank=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='class_id', null=True, blank=True)
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE, db_column='topic_id', null=True, blank=True)
    page_img_path = models.FileField(upload_to=exam_paper_path)
    status = models.IntegerField(default=default_status, choices=status_choice)

    class Meta:
        managed = False
        db_table = 'ingestion'
        

