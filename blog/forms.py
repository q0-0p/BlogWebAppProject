from django import forms
from .models import Post, Author
import datetime


class CreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    created_date = forms.DateTimeField(initial=datetime.datetime.now())


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'bio')


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'created_date')
