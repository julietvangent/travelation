from django import forms

from .models import Post, DestinationsPost, PracticalPost, OtherPost, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DestPostForm(forms.ModelForm):

    class Meta:
        model = DestinationsPost
        fields = ('title', 'text',)

class PracPostForm(forms.ModelForm):

    class Meta:
        model = PracticalPost
        fields = ('title', 'text',)

class OtherPostForm(forms.ModelForm):

    class Meta:
        model = OtherPost
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
