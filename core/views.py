
from django.http import HttpResponse
from django.shortcuts import render

# Postoji funkcija home koja prikazuje nekakvu poruku "Hello world"
# Gde se prikazuje ova funkcija?
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is my about page")