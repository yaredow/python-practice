from django.http import HttpResponse


# Create your views here.
def HomePage(request):
    return HttpResponse("Hello, world!")
