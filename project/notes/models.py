from django.db import models


class Label(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=510)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, blank=True, null=True)
