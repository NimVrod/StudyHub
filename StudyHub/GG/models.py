from django.db import models

# Create your models here.


class Section(models.Model):
    """
    Section model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RIP(models.Model):
    """
    Dead gamer model
    """
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name