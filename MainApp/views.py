from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    text = "Welcome!"
    return HttpResponse(text)

def about(request):
    text = "Автор: Евгений"
    return HttpResponse(text)