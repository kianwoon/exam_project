from django.contrib import admin
from .models import Schools

# Register your models here.
class SchoolForm(admin.ModelAdmin):
    list_filter = ('grade',)
    ordering=('school_name',)

admin.site.register(Schools, SchoolForm)
