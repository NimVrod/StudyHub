from django.forms import ModelForm, inlineformset_factory
from .models import quiz, pytanie, odpowiedz


class QuizForm(ModelForm):
    class Meta:
        model = quiz
        fields = ['name']


class PytanieForm(ModelForm):
    class Meta:
        model = pytanie
        fields = ['name']


class OdpowiedzForm(ModelForm):
    class Meta:
        model = odpowiedz
        fields = ['name', 'is_correct']



