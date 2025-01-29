# core/urls.py

from django.urls import path
from .views import HomeView, AboutView, ProjectsView, ContactView
app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
]
