from django.db import models


# Create your models here.
class quiz(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateField()
    img = models.CharField()

    def __str__(self):
        return self.name


class pytanie(models.Model):
    name = models.CharField(max_length=200)
    q = models.ForeignKey(quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class odpowiedz(models.Model):
    name = models.CharField(max_length=200)
    p = models.ForeignKey(pytanie, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name
