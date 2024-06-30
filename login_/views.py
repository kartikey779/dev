from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def patient(request):
    return HttpResponse("<h1>This is patient dashboard</h1>")
def doctor(request):
    return HttpResponse("<h1>This is doctor dashboard</h1>")