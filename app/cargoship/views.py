from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import docker
import json


@login_required(redirect_field_name="")
def index(request):
    return render(request, "cargoship/index.html", {})


@login_required(redirect_field_name="")
def containers(request):
    client = docker.from_env()
    if request.method == "POST":
        id = request.POST.get("id")
        if "start" in request.POST:
            client.containers.get(id).start()
        elif "restart" in request.POST:
            client.containers.get(id).restart()
        elif "stop" in request.POST:
            client.containers.get(id).stop()

    running = client.containers.list(all=True)
    containers = [make_container_entry(cont) for cont in running]
    return render(request, "cargoship/containers.html", {"containers": containers})


def make_container_entry(container):
    entry = {
        # "attrs": container.attrs,
        "id": container.id,
        "id_attribute": container.id_attribute,
        "image": container.image.tags[0],
        # "labels": container.labels,
        "name": container.name,
        "ports": container.ports,
        "short_id": container.short_id,
        "status": container.status,
    }
    return entry


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form["username"].value(), password=form["password"].value())
            if user:
                login(request, user)
                return redirect("index")
            else:
                form.add_error("", "Failed to login, please try again.")
                return redirect("login")
    else:
        form = LoginForm()
    return render(request, "cargoship/login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(
                    username=form["username"].value(), email=form["email"].value(), password=form["password"].value()
                )
            except:
                form.add_error("", "Username or email already taken.")
            else:
                return redirect("login")
    else:
        form = SignUpForm()

    return render(request, "cargoship/signup.html", {"form": form})
