from django import forms
from .models import pessoas

class formularioPessoa(forms.ModelForm):
    class Meta:
        model = pessoas
        fields = ('nome', 'idade')