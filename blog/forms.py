from .models import Comment, Reply, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ''}

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)
        labels = {'body': ''}

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','category','image')

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= ('name',)