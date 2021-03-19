from django.shortcuts import render
from .models import Famous
def list(request):
    famous_list = Famous.objects.all()
    context = {'famous_list': famous_list}
    return render(request, 'people/index.html', context)
