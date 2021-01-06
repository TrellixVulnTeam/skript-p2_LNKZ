from django.shortcuts import render
from .models import Note, Label
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def index(request):
    tmp_notes = Note.objects.filter(owner=request.user)
    labels = Label.objects.filter(owner=request.user)
    pinned = [x for x in tmp_notes if x.pinned]
    notes = set(tmp_notes) - set(pinned)
    return render(request, 'notes/index.html', {'notes': notes, 'labels': labels, 'pinned': pinned})
