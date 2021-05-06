from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField("Имя",max_length=120)
    surname = models.CharField("Фамилие",max_length=120)
    age = models.IntegerField("Возраст")
    ilness = models.CharField("Болезнь",max_length=120)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"