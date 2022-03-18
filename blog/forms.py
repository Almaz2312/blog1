from django import forms
from blog.models import Blog


# Первый вариант создания
# class BlogForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     description = forms.CharField(max_length=200, widget=forms.TextInput({}))
#     author = forms.IntegerField()
#

# Второй вариант создания
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"