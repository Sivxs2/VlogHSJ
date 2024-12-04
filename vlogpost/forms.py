from django.forms import ModelForm
from .models import VlogPost


class ContentForm(ModelForm):
    class Meta:
        model = None
        fields = [] 


class Vlogform(ContentForm):
    class Meta(ContentForm.Meta):
        
        fields = ['title', 'video_url', 'description', 'author', 'published_date', 'tags' ]

