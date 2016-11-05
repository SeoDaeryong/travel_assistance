from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('lat', 'lng', 'place_id', 'place_name', 'group_name')

class UpdatePlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('id', 'lat', 'lng', 'place_id', 'place_name', 'info', 'capital', 'group_name')
