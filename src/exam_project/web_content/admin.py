from django.contrib import admin
from .models import WebContent

# Register your models here.

class WebContentAdmin(admin.ModelAdmin):
    list_filter = ('auth_group',)
    list_display = ('id' , 'title', 'subtitle', 'body',)
    list_editable = ('title', 'subtitle', 'body',)
    list_display_links = ('id',)

admin.site.register(WebContent, WebContentAdmin)