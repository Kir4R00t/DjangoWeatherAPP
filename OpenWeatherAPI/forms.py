from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label='Enter a city name', max_length=100)
