# Generated by Django 3.2.8 on 2021-10-29 12:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название книги')),
                ('author', models.CharField(max_length=127, verbose_name='Автор')),
                ('publisher', models.CharField(max_length=127, verbose_name='Извдатель')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('number', models.IntegerField(verbose_name='Количество')),
                ('about', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Имя')),
                ('surname', models.CharField(max_length=127, verbose_name='Отчество')),
                ('patronymic', models.CharField(max_length=127, verbose_name='Фамилия')),
                ('home_adress', models.CharField(max_length=127, verbose_name='Адресс жительства')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateTimeField(auto_now=True, verbose_name='')),
                ('date_of_delivery', models.DateTimeField(verbose_name='')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.book', verbose_name='')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.reader', verbose_name='')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
    ]
