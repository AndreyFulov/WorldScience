from django.shortcuts import render
from .models import Center

def centres(request):
    return render()

def detail(request, center_id):
    center = Center.objects.get(pk=center_id)
    return render(request, "centres/detail.html", {'center' : center})

