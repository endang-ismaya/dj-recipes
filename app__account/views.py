from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from app__account.forms import UserProfileForm


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

            return redirect("foodie:index")

    context = {"form": form}
    return render(request, "app__account/register.html", context)


def edit_user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect("foodie:index")
    else:
        form = UserProfileForm(instance=request.user.profile)

    return render(request, "registration/edit_profile.html", {"form": form})
