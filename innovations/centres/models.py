from django.db import models
from django_quill.fields import QuillField

class Center(models.Model):
    center_id = models.IntegerField(default=0)
    center_Name = models.CharField(max_length=256)
    center_desc = models.TextField()
    center_photo = models.TextField()
    center_link = models.TextField(default="google.com")
    def __str__(self):
        return self.center_Name
