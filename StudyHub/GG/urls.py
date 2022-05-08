from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<int:section_id>', views.detail, name='section'),
    path('userinfo/<int:user_id>', views.user_info, name='userinfo'),
    path('adduser/', views.add_user, name='adduser'),
]
