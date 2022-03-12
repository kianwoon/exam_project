from django import forms
from .models import UserSubscription 

import datetime
from datetime import date

class subscription_form(forms.ModelForm):
    
    class Meta:
        model = UserSubscription 
        fields = ['subscription_id']
#        exclude=['username','subscription_date','subscription_end']        

    def __init__(self, *args, **kwargs):
        super(subscription_form, self).__init__(*args, **kwargs)
        self.fields['subscription_id'].label = "Subscription package"
    


