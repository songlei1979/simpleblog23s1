from django.forms import ModelForm, TextInput, Textarea, Select

from blog.models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'author', 'post_image']

        widgets={
            'title': TextInput(attrs={'class':'form-content', 'placeholder':'Title Blarblar'}),
            'body': Textarea(attrs={'class':'form-content'}),
            'category': Select(attrs={'class':'form-control'}),
            'author': Select(attrs={'class': 'form-control'}),
        }

