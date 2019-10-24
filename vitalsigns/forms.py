from django import forms

class VitalsForm(forms.Form):
    vitals = forms.CharField(widget=forms.Textarea)
    vitals1 = forms.CharField(widget=forms.Textarea)
    vitals3 = forms.CharField(widget=forms.Textarea)
