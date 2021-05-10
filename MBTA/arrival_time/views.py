from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Stop, Comment

# Load the default view and display stops the user is tracking if there are any.
def index(request):
    # Try to querry for stops the user is tracking
    try:
        stops = request.user.tracking.all()
    except:
        # If exception from no stops being tracking, then return the index.html without the stop object
        return render(request, "arrival_time/index.html")
    return render(request, "arrival_time/index.html", {
        "stops": stops
    })

# View to load the HTML page for searching the MBTA stops
def search(request):
    return render(request, "arrival_time/add_stop.html")

# Save a comment to the database
@login_required
def comment(request, stop_id):
    # Check for Post Request when a user creates a new comment
    if request.method == "POST":
        text = request.POST["comment"]
        # Get the stop associated with the comment. Stop.id pass through url argument stop_id
        stop = get_object_or_404(Stop, pk=stop_id)
        comment = Comment(author=request.user, text=text, stop=stop)
        comment.save()
        return HttpResponseRedirect(reverse("stop", args=(stop_id,)))

# View for specific train or bus stop info
def display_stop(request, stop_id):
    stop = Stop.objects.get(id=stop_id)
    # refrenced this site https://www.youtube.com/watch?v=iwNBwG8RBok for querrying a one to many relationship
    comments = Comment.objects.filter(stop__id=stop_id).order_by("-date_created")
    return render(request, "arrival_time/stop.html", {
        "stop": stop,
        "comments": comments
    })

# API view to save a users favorite stop to the database
@login_required
def save_stop(request):
     # Check for POST Request when saving a new stop
    if request.method == "POST":
        stop = get_object_or_404(Stop, name=request.POST["stop"])
        # Add the stop to the logged in users tracking database
        request.user.tracking.add(stop)
        return HttpResponseRedirect(reverse("index"))
    # Default behavior to load the add stop page
    else:
        return render(request, "arrival_time/add_stop.html")

# Copied from Project 4. Modified url paths
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


# Copied from Project 4. Modified url paths
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Copied from Project 4. Modified url paths
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

