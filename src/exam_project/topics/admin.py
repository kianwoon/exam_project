from django.contrib import admin
from .models import Topics
from classes.models import Classes


# Register your models here.
class topicadmin(admin.ModelAdmin):
    list_display = ['class_id', 'topic_name']
    readonly_fields = ['topic_id']
    search_fields = ['topic_name']
    

admin.site.register(Topics, topicadmin)