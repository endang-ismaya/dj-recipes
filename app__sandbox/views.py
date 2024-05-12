from django.shortcuts import render


def index(request):
    return render(request, "app__sandbox/index.html", {})
