from django.http import HttpResponse


def recipes(request):
    return HttpResponse("Recipe Page")
