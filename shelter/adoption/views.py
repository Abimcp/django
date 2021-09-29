from django.shortcuts import render, get_object_or_404
from .models import dog_info
from .models import Dog

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
        
def dogs(request):
    data = {'doggos': Dog.objects.all()}
    return render(request, 'dogs.html', data)

def show(request, id):
    dog = get_object_or_404(Dog, pk=id)
    data = {'dog': dog } 
    return render(request, 'show.html', data)

def not_found_404(request, exception):
    data = {'err': exception}
    return render(request, '404.html', data)

def not_found_500(request, exception):
    return render(request, '500.html')

