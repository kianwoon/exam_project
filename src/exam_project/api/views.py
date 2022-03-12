from django.shortcuts import render
from api.models import Announcement
from rest_framework import viewsets
from rest_framework import permissions
import datetime
from api.serializer import Announcement_Marqee
# Create your views here.

class Announcement_Marqee(viewsets.ModelViewSet):
    queryset = Announcement.objects.filter(status=1).filter(valid_till__gte=datetime.date.today())
    serializer_class = Announcement_Marqee
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

