from django.db import models
import uuid 

# Create your models here.
class Schools(models.Model):
    school_id = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=45)
    school_name = models.CharField(max_length=100, db_column='school_name')
    school_rank = models.IntegerField()
    school_population = models.IntegerField()
    school_address = models.CharField(max_length=100)  
    grade = models.CharField(max_length=100, db_column='grade')

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.topic_id}, {self.topic_name}, {self.class_id}'
        return '%s' % (self.school_name)
    

    class Meta:
        managed = False
        db_table = 'schools'
        