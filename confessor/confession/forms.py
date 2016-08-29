from django import forms
from .models import Confession

class confessionForm(forms.Form):
    confession = forms.CharField(max_length=300)

class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ["confession", "id"]
