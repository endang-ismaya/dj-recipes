from django.http import HttpResponse


def comments(request):
    return HttpResponse("Comment Page")
