from django import forms

class NameForm(forms.Form):
    dev_name = forms.CharField(label='Device name', max_length=100)