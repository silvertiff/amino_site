from django import forms
from .models import AminoAcid

class AminoAcidForm(forms.ModelForm):
    class Meta:
        model = AminoAcid
        fields = ['name', 'three_letter_code', 'one_letter_code', 'structure_image', 'description']

class QuizForm(forms.Form):
    answer = forms.CharField(label="Ваш ответ", max_length=50)
