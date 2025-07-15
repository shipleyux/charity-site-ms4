from django.apps import AppConfig
from django import forms

class DonationForm(forms.Form):
    amount = forms.DecimalField(label="Donation Amount (£)", min_value=1, decimal_places=2)

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
