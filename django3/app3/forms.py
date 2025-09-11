from django import forms
class inputform(forms.Form):
    p = forms.IntegerField(min_value=1000, max_value=100000, label="Enter principal amount")
    t = forms.IntegerField(min_value=1, max_value=10, label="Enter time in years")
    r = forms.IntegerField(min_value=3, max_value=12, label="Enter rate of interest as %")
