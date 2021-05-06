from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.name, self.surname, self.age)
    
    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Докторы"