from django import forms
from .models import Otziv


# первый способ создать новую модель
# class OtzivForm(forms.Form):
#     name = forms.CharField(label='Имя', required=True)
#     otziv = forms.CharField(label='Текст отзыва', required=True, widget=forms.Textarea(attrs={'rows': 5, 'cols': 70}))

# второй способ на основе созданной модели
class OtzivForm(forms.ModelForm):
    class Meta:
        model = Otziv
        fields = ['name','otziv']
        labels = {'name':'Имя', 'otziv':'Отзыв'}
        error_messages = {'name': {'max_lenght': 'Слишком большое имя'}}