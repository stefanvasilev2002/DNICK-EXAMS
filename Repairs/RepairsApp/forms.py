from django import forms
from .models import Repair


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
