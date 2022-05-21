from django.db import models

# Create your models here.


class Section(models.Model):
    """
    Section model
    """
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name

class RIP(models.Model):
    """
    Dead gamer model
    """
    name = models.CharField(max_length=100, blank=False, unique=True)
    date = models.DateField(blank=False)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name