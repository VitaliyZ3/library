from django.db import models
from django.db.models.deletion import DO_NOTHING
from phonenumber_field import modelfields
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=127, verbose_name='Назва книги')
    author = models.CharField(max_length=127, verbose_name='Автор')
    publisher = models.CharField(max_length=127, verbose_name='Видавник')
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name='Фото')
    number = models.IntegerField(verbose_name='Кількість')
    about = models.TextField(verbose_name='Опис')

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        return f'Книга "{self.name}"'


class Ticket(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Відвідувач', blank=True, null=True)
    date_of_delivery = models.DateTimeField(verbose_name='Дата здачі')
    book = models.ForeignKey(Book, on_delete=DO_NOTHING, verbose_name='Книга', blank=True, null=True)

    class Meta():
        verbose_name = 'Білет'
        verbose_name_plural = 'Білети'

    def __str__(self) -> str:
        return f'Білет "{self.reader.username} " '
