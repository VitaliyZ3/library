from django.db import models
from django.db.models.deletion import DO_NOTHING
from phonenumber_field import modelfields
import phonenumber_field
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
from datetime import datetime
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название книги')
    author = models.CharField(max_length=127, verbose_name='Автор')
    publisher = models.CharField(max_length=127, verbose_name='Извдатель')
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name='Фото')
    number = models.IntegerField(verbose_name='Количество')
    about = models.TextField(verbose_name='Описание')

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

class Reader(models.Model):
    name = models.CharField(max_length= 127, verbose_name='Имя')
    surname = models.CharField(max_length= 127, verbose_name='Отчество')
    patronymic = models.CharField(max_length= 127, verbose_name='Фамилия')
    home_adress = models.CharField(max_length=127, verbose_name='Адресс жительства')
    phone = PhoneNumberField(null = False, blank = False, verbose_name = 'Номер телефона')

    class Meta():
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self) -> str:
        return f'Читатель "{self.name} {self.surname}" '

class Ticket(models.Model):
    reader = models.ForeignKey(Reader, on_delete=DO_NOTHING, verbose_name='')
    date_of_issue = models.DateTimeField(auto_now=datetime.now(), verbose_name='')
    date_of_delivery = models.DateTimeField(verbose_name='')
    book = models.ForeignKey(Book, on_delete=DO_NOTHING, verbose_name='')

    class Meta():
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self) -> str:
        return f'Билет "{self.reader.name} {self.book.name}" '
