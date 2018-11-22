from django.db import models

class Jobadd(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return '{} ({})'.format(self.title, self.description)
