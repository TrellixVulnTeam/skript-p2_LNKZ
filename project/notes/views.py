from django.shortcuts import render, redirect
from .models import Note, Label
from .forms import NotesForm
from django.contrib import messages
import logging
from django.contrib.auth.decorators import login_required, permission_required

logger = logging.getLogger(__name__)


@login_required
def index(request):
    tmp_notes = Note.objects.filter(owner=request.user)
    labels = Label.objects.filter(owner=request.user)
    pinned = [x for x in tmp_notes if x.pinned]
    notes = set(tmp_notes) - set(pinned)
    return render(request, 'notes/index.html', {'notes': notes, 'labels': labels, 'pinned': pinned})


@login_required
def notes_edit(request, id):
    if request.method == 'POST':
        form = NotesForm(request.POST)

        if form.is_valid():
            note = Note.objects.filter(owner=request.user).get(id=id)
            note.title = form.cleaned_data['title']
            note.pinned = form.cleaned_data['pinned']
            note.content = form.cleaned_data['content']
            note.label = form.cleaned_data['label']
            note.save()
            messages.success(request, 'Note edited successfully')
            return redirect('notes:index')
        else:
            return render(request, 'notes/edit.html', {'form': form, 'id': id})
    else:
        note = Note.objects.get(id=id)
        form = NotesForm(instance=note)
        return render(request, 'notes/edit.html', {'form': form, 'id': id})


@login_required
def notes_delete(request, id):
    if request.method == 'POST':
        note = Note.objects.filter(owner=request.user).get(id=id)
        note.delete()
        messages.success(request, 'Note deleted successfully')
    return redirect('notes:index')


@login_required
def notes_create(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = Note()
            note.title = form.cleaned_data['title']
            note.pinned = form.cleaned_data['pinned']
            note.content = form.cleaned_data['content']
            note.label = form.cleaned_data['label']
            note.owner = request.user
            note.save()
            messages.success(request, 'Note created successfully')
            return redirect('notes:index')
        else:
            return render(request, 'notes/create.html', {'form': form })
    else:
        form = NotesForm()
        form.fields['label'].queryset = Label.objects.filter(owner_id=request.user.id)
        return render(request, 'notes/create.html', {'form': form})
