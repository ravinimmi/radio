from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at radio homepage.")
