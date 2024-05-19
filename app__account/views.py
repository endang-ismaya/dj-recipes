from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render


def user_register(request):
    """User Registration"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # log the user in
            login(request, new_user)

            return HttpResponse("User created!")

    context = {"form": form}
    return render(request, "app__account/register.html", context)
