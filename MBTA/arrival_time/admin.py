from django.contrib import admin
from .models import User, Stop, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Stop)
admin.site.register(Comment)