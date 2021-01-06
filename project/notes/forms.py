from django.forms import ModelForm, models
from .models import Note, Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['title', 'color']


class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'label', 'pinned']