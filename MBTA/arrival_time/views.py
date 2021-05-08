from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Stop, Comment
# Create your views here.


def index(request):

    stops = request.user.tracking.all()

    return render(request, "arrival_time/index.html", {
        "stops": stops
    })

def search(request):
    return render(request, "arrival_time/add_stop.html")

# Save a comment to the database
def comment(request, stop_id):
    # # Check for Post Request when a user creates a new comment
    if request.method == "POST":
        text = request.POST["comment"]
        stop = get_object_or_404(Stop, pk=stop_id)
        comment = Comment(author=request.user, text=text, stop=stop)
        comment.save()
        return HttpResponseRedirect(reverse("stop", args=(stop_id,)))

# View for specific train or bus stop info
def display_stop(request, stop_id):
    stop = Stop.objects.get(id=stop_id)
    # refrenced this site https://www.youtube.com/watch?v=iwNBwG8RBok
    comments = Comment.objects.filter(stop__id=stop_id).order_by("-date_created")

    return render(request, "arrival_time/stop.html", {
        "stop": stop,
        "comments": comments
    })



def save_stop(request):
     # Check for Post Request when saving a new stop
    if request.method == "POST":
        # pk=int(request.POST["stop"])
        stop = get_object_or_404(Stop, name="Malden Center")
        request.user.tracking.add(stop)
        #stop.tracking = User.objects.get(pk=request.user.id)
        #stop.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        # Default behavior to load the posts
        return render(request, "arrival_time/add_stop.html")

# Copied from Project 4
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "arrival_time/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "arrival_time/login.html")


# Copied from Project 4
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Copied from Project 4
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "arrival_time/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "arrival_time/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "arrival_time/register.html")

