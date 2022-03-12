from django.db import models

# Create your models here.

class WebContent(models.Model):
    
    default_status=0
    status_choice = [
        (default_status, 'OFF'),
        (1, 'LIVE')
    ]

    default_style='card text-white bg-primary mb-3'
    style_choice = [
        ('card text-white bg-primary mb-3', 'Blue'),
        ('card text-white bg-secondary mb-3', 'Black'),
        ('card text-white bg-success mb-3', 'Green'),
        ('card text-white bg-danger mb-3', 'Red'),
        ('card text-white bg-warning mb-3', 'Orange'),
        ('card text-white bg-info mb-3', 'Purple'),
        ('card bg-light mb-3', 'Gray')
    ]
    default_auth_group =0
    auth_group_choices = [
        (0, 'public'),
        (1, 'registered'),
        (2, 'subscribed'),
    ]
    


    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    style = models.CharField(max_length=100, blank=True, null=True, choices=style_choice, default=default_style)
    status = models.IntegerField(blank=True, null=True, choices=status_choice, default=default_status)
    links = models.CharField(max_length=300, blank=True, null=True, default='#')
    auth_group = models.IntegerField(default=default_auth_group, choices=auth_group_choices)

    def __str__(self):
        """String for representing the Model object."""
#        return f'{self.class_id}, {self.class_description}, {self.class_level}'
        return '%s %s -- [[%s]]' % (self.title, self.subtitle, self.style)    

    class Meta:
        managed = False
        db_table = 'web_content'