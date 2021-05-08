from django.db.models import fields
from django.forms import ModelForm
from .models import User, Post

# Creates the form on create_listing.html that allows users to add an auction listing to the site.
class NewPostForm(ModelForm):
    class Meta:
        model = Stop
        fields = ["message"]


