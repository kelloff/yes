# Django
from django import forms

# Local
from main.models import (Pen , Stock)

class PenForm(forms.ModelForm):
    """Pen form."""

    class Meta:
        model = Pen
        fields = '__all__'
        
        
    