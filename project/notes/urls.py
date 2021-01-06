
from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter/<int:label_id>',views.index, name='filter'),
    path('notes/<int:id>', views.notes_edit, name='edit'),
    path('notes/delete/<int:id>', views.notes_delete, name='delete'),
    path('notes/create', views.notes_create, name='create'),
    path('labels/<int:id>', views.labels_edit, name='labels_edit'),
    path('labels/delete/<int:id>', views.labels_delete, name='labels_delete'),
    path('labels/create', views.labels_create, name='labels_create'),


]
