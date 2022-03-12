from rest_framework import serializers
from .models import Announcement

class Announcement_Marqee(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Announcement
        fields = ['msg_body']
        
    