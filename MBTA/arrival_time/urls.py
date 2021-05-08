
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stop/<int:stop_id>", views.display_stop, name="stop"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("comment/<int:stop_id>", views.comment, name="comment"),
    
    # API path to save stops
    path("save-stop", views.save_stop, name="save-stop")
]

