# Generated by Django 5.0.1 on 2024-02-06 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='creator',
        ),
    ]
