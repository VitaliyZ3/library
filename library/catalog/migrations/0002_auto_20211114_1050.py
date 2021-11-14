# Generated by Django 3.2.8 on 2021-11-14 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Білет', 'verbose_name_plural': 'Білети'},
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date_of_issue',
        ),
        migrations.AlterField(
            model_name='book',
            name='about',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=127, verbose_name='Назва книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.IntegerField(verbose_name='Кількість'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=127, verbose_name='Видавник'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_of_delivery',
            field=models.DateTimeField(verbose_name='Дата здачі'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Відвідувач'),
        ),
        migrations.DeleteModel(
            name='Reader',
        ),
    ]