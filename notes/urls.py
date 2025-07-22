from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
    path('notes/pop', views.PopularNotesListView.as_view()),

    # path('notes/<int:pk>', views.detail),
]
