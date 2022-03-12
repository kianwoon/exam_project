from django.contrib import admin
from .models import Classes
from topics.models import Topics 

# Register your models here.
class topicsform(admin.StackedInline):
    model = Topics
    extra = 0
    readonly_fields = ('class_id',)
 #   fields = ['class_id','topic_name']

class classform(admin.ModelAdmin):
    inlines = [topicsform]
#    list_display = ['class_description','class_level']
#    search_fields = ['class_description']

admin.site.register(Classes, classform)