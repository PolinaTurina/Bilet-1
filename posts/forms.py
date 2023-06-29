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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')

    name = forms.CharField(max_length = 50,
                           min_length = 3,
                           label = "Ваше имя",
                           widget = forms.TextInput(attrs={'placeholder': 'Кошкин Кот Котович'}))
    text = forms.CharField(max_length=600, 
                           label = "Комментарий", 
                           widget = forms.Textarea(attrs={'cols':50, 'rows': 5, 'placeholder': 'Напишите пару слов...'}))
