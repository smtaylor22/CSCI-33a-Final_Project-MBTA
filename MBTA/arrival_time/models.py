from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    tracking = models.ManyToManyField("Station", related_name="trackers")

class Station(models.Model):
    # MBTA stop id associated with stop ---- so can querry for this stop prediction later 
    mbta_id = models.IntegerField()
    # Stop name - Name of the stop the user is tracking
    name = models.CharField(max_length=255)
    # Associated line with Stop (eg. Subway: Red line, Bus: 70)
    line = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} - {self.line}"

# Comments - User comments and info associated with a station/stop
class Comment(models.Model):
    # Text for comments - removes requirement for comments
    text = models.TextField(blank=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="authors")
    created = models.DateTimeField(auto_now_add=True)
    station = models.ForeignKey("Station", on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.content