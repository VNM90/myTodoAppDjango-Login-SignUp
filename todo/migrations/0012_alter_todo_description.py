# Generated by Django 3.2.2 on 2021-06-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210606_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]