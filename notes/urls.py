"""
URL patterns for the notes app.
This module maps URLs to views for the notes app.
"""
from django.urls import path
from . import views


urlpatterns = [
    # Homepage - list all notes
    path('', views.note_list, name='note_list'),

    # View a single note
    path('<int:pk>/', views.note_detail, name='note_detail'),

    # Create a new note
    path('new/', views.note_create, name='note_create'),

    # Edit an existing note
    path('<int:pk>/edit/', views.note_update, name='note_update'),

    # Delete a note
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
