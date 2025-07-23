from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView, DetailView, ListView
# Create your views here.
from .forms import NotesForm
from .models import Notes

class NotesListView(ListView):
   model = Notes
   context_object_name = "notes"
   template_name = "notes/notes_list.html"


class PopularNotesListView(ListView):
   model = Notes
   context_object_name = "notes"
   template_name = "notes/notes_list.html"
   queryset = Notes.objects.filter(likes__gt=0) #gt = greater than


class NotesDetailView(DetailView):
   model = Notes
   context_object_name = "note"


class NotesCreateView(CreateView):
   model = Notes
   success_url = '/smart/notes'
   form_class = NotesForm


class NotesUpdateView(UpdateView):
   model = Notes
   success_url = '/smart/notes'
   form_class = NotesForm   




# def list(request):
#     all_notes = Notes.objects.all()
#     return render (request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist: 
#         return render (request, 'notes/notes_not_found.html', {})
#     return render(request,'notes/notes_detail.html',{'note':note})