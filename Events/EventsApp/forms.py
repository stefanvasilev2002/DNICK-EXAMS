from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user', 'num_participants',]
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'is_open':
                visible.field.widget.attrs["class"] = "form-check-input"

