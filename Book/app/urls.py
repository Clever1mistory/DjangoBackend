from django.urls import path, include, re_path
from .views import auth

urlpatterns = [
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path('__debug__/', include('debug_toolbar.urls')),

]