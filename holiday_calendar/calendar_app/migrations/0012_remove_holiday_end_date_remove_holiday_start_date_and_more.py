# Generated by Django 4.2.11 on 2024-04-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0011_alter_holiday_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='holiday',
            name='start_date',
        ),
        migrations.AddField(
            model_name='holiday',
            name='date',
            field=models.DateField(default='2000-01-01', verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='hashtags',
            field=models.ManyToManyField(to='calendar_app.hashtag', verbose_name='Хэштеги'),
        ),
    ]