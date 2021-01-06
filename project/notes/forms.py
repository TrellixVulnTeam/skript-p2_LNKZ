from django.forms import ModelForm, BooleanField
from .models import Note, Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['title']


class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'label', 'pinned']
