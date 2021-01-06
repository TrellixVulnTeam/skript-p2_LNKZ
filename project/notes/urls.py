
from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('notes/<int:id>', views.notes_edit, name='edit'),
    path('notes/delete/<int:id>', views.notes_delete, name='delete'),
]
