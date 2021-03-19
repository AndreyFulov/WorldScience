from django.db import models

class Famous(models.Model):
    famous_name = models.CharField(max_length=128)
    famous_desc = models.TextField()
    famous_source = models.TextField()
    famous_photo = models.TextField()
    def __str__(self):
        return self.famous_name

