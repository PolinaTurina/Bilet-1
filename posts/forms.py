from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'text', 'image')
        fields = '__all__' #нужно показывать все поля, кроме тех, которые заполняются автоматически - например ДАТА
    title = forms.CharField(max_length=50, label='Заголовок')
    text = forms.CharField(max_length=1000, label='Текст',
                          widget = forms.Textarea(attrs={'cols':50, 'rows':7}))
    image = forms.ImageField(required=False)