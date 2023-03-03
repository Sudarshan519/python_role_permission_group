from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from . create_super_user import create_admin
from .permissions import create_group,create_permission
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
   openapi.Info(
      title="CLONE RPS API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

 
# create_group()
# create_permission()
# create_admin()
# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'register', views.RegisterView.as_view(),basename="user")
# router.register(r'users', views.UserViewSet,basename="user")
# router.register(r'login',views.LoginView.as_view(),basename='login')
# router.register(r'post',views.PostListView.as_view(),basename="post")
# router.register(r'auth', include('djoser.urls'),basename='auth'),
urlpatterns = [
    path('',include('djoser.urls') ),
  path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
   # path('auth',include('djoser.urls')),
path('', include(router.urls)),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
