from django.contrib import admin

# Register your models here.
from .models import UserSubscription

class UserSubscriptionForm(admin.ModelAdmin):
    list_display = ['username','subscription_date','subscription_end','transaction_id']
    search_fields = ['username','transaction_id']
    readonly_field = ['transaction_id']
    
admin.site.register(UserSubscription)

