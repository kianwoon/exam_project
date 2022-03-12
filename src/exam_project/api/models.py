from django.db import models

# Create your models here.
class Announcement(models.Model):
    default_style=0
    style_choice = [
        (default_style, 'OFF'),
        (1, 'LIVE')
    ]

    msg_body = models.TextField(max_length=500)
    status = models.IntegerField(choices=style_choice, default=default_style)
    valid_till = models.DateTimeField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.msg_body)

    class Meta:
        managed = False
        db_table = 'announcement'