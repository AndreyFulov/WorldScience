from django.shortcuts import render
from centres.models import Center
from people.models import Famous
from django.db.models import Q

def index(request):
    return render(request, 'main/index.html')

def post_list(request):

    search_query = request.GET.get('search', '')
    if search_query:
        centres = Center.objects.filter(Q(center_Name__contains=search_query) | Q(center_desc__contains=search_query))
        people = Famous.objects.filter(Q(famous_name__contains=search_query) | Q(famous_desc__contains=search_query))
    else:
        centres = Center.objects.all()
        people = Famous.objects.all()

    context = {'centres' : centres,
               'people' : people}
    return render(request, 'main/posts.html', context)
