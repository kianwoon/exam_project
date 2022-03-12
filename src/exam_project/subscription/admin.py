from django.contrib import admin
from .models import Subscription
# Register your models here.


class subadmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'price']
    readonly_fields=['subscription_id']


admin.site.register(Subscription, subadmin)
