from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(verbose_name="Description")
    rate = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
