from django import forms
from Health.models import Patient
from django.forms.widgets import NumberInput

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"


    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        

        
        self.fields['pdate'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        for c in self.fields.values():
            c.widget.attrs['class'] = 'form-control'
        