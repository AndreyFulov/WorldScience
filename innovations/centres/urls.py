from django.views.generic.list import ListView
from django.urls import path, include
from . import views
from .models import Center

urlpatterns = [
    path('', ListView.as_view(queryset=Center.objects.all(), template_name="centres/allcentres.html"), name="centres"),
    path('<int:center_id>/', views.detail, name='detail')
]