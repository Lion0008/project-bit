# bitcoin_app/forms.py
from django import forms

class BitcoinProfitForm(forms.Form):
    irrupto_selector = forms.CharField(label='Irrupto Selector', max_length=100)
    period = forms.CharField(label='Period', max_length=100)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
