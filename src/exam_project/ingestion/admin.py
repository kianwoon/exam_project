from django.contrib import admin
from .models import Ingestion

# Register your models here.
class IngestionForm(admin.ModelAdmin):
    # fields = ('school_id','class_id','topic_id')
    list_display= ('school_id','class_id','topic_id', 'page_img_path')

admin.site.register(Ingestion, IngestionForm)