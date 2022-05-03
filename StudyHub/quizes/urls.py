from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quiz_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
]
