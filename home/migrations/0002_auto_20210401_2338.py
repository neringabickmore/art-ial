# Generated by Django 3.1.5 on 2021-04-01 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='img',
        ),
        migrations.RemoveField(
            model_name='about',
            name='url',
        ),
    ]
