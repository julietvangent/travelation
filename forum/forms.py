from django import forms

from .models import Post, DestinationsPost, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DestPostForm(forms.ModelForm):

    class Meta:
        model = DestinationsPost
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
