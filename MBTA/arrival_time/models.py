from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    tracking = models.ManyToManyField("Stop", related_name="tracked_stations")

class Stop(models.Model):
    # MBTA stop id associated with stop ---- so can querry for this stop prediction later 
    mbta_id = models.IntegerField()
    # Stop name - Name of the stop the user is tracking
    name = models.CharField(max_length=255)
    # Associated line with Stop (eg. Subway: Red line, Bus: 70)
    line = models.CharField(max_length=255)
    # Attribute to track the direction or end destination of the route for the stop
    direction = models.CharField(max_length=255)

    
    def __str__(self):
        return f"{self.name} - {self.line} - {self.direction}"

    


# Comments - User comments and info associated with a Stop
class Comment(models.Model):
    # Text for comments - removes requirement for comments
    text = models.TextField(blank=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="authors")
    date_created = models.DateTimeField(auto_now_add=True)
    stop = models.ForeignKey("Stop", on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f"{self.author} - {self.text}"

