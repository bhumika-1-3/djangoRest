from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
import json
# page restriction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_page_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist :(')

        # error or give a user object of the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # create a session id in the cookies
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username or password invalid :(')

    context = {

    }
    return render(request, 'login_register.html', context)


def logout_page_view(request):
    # deletes the session token
    logout(request)
    return redirect('home')


def home_view(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''
#    contain minimun few letters and not case sensitive
    rooms = Room.objects.filter(topic__name__icontains=q)
    topic = Topic.objects.all()

    room_count = rooms.count()
    context = {
        'rooms': rooms,
        'topic': topic,
        'room_count': room_count,
    }
    return render(request, 'home.html', context)


def room_view(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {
        'room': rooms
    }
    return render(request, 'room.html', context)


# page restriction
@login_required(login_url='/login')
def create_room_view(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'RoomForm': form,
    }
    return render(request, 'room_form.html', context)


@login_required(login_url='/login')
def update_room_view(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host_user:
        return HttpResponse("<h1>YOU ARE NOT ALLOWED!</h1>")
    if request.method == "POST":
        # tell where to replace data
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'RoomForm': form,
    }
    return render(request, "room_form.html", context)


@login_required(login_url='/login')
def delete_room_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj': room})


def trial_view(request):
    data = {
        'bhumi': '34',
        'om': '54',
        'prachi': '23',
        'anaida': '3',
    }
    # converts single quotes to double as JSON format
    jsonData = json.dumps(data)
    print(jsonData)
    return HttpResponse("<h1>try</h1>")
