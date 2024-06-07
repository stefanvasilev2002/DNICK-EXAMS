from django import forms
from .models import *


class HotelReservationForm(forms.ModelForm):
    class Meta:
        model = HotelReservation
        exclude = ['user', '']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(HotelReservationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'is_confirmed':
                visible.field.widget.attrs['class'] = 'form-check-input'
