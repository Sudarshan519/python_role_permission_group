from django.contrib import admin
from django.urls import path
from . import views
from . create_super_user import create_admin
from .permissions import create_group,create_permission
create_group()
create_permission()
create_admin()
urlpatterns = [
    path('',views.PostListView.as_view()),
    
]
