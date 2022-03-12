from django.db import models
import uuid
from django.urls import reverse


# Create your models here.
class Classes(models.Model):
    class_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    class_description = models.CharField(max_length=100)
    class_level = models.IntegerField()



    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '%s' % (self.class_description)

    def get_absolute_url(self):
        return reverse('topics:view_topic_by_classid', kwargs={'id':self.class_id})

    class Meta:
        db_table = 'classes'
    

#http://192.168.1.154:8080/%5Etopics/(%3FPbc42dcd9-694b-41ce-b039-3e3d8e246633%5B%5Cw-%5D+)/$