from django.db import models
from django.urls import reverse


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:15] + '...'

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk, })
