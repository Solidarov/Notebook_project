"""
URL configuration for untitle_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import (NotesListView,
                    NotesDetailView,
                    NotesCreateView,
                    NotesUpdateView,
                    NotesDeleteView,
                    AboutPageTemplateView)

urlpatterns = [
    path('', NotesListView.as_view(), name='notebook-home'),
    path('about/', AboutPageTemplateView.as_view(), name='notebook-about'),

    path('note/<int:pk>/', NotesDetailView.as_view(), name='note-detail'),
    path('note/new/', NotesCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', NotesUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NotesDeleteView.as_view(), name='note-delete'),
]
