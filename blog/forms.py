from django.forms import ModelForm 
from .models import *
class CommentForm(ModelForm):
    class Meta:
        model=Comments
        exclude=["post"]
        labels={
            "user_name":"Your Name",
            "email":"Email",
            "comment":"Comment",
            
        }
