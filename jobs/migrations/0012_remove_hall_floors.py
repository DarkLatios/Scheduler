# Generated by Django 3.0.5 on 2021-01-11 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20210111_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='floors',
        ),
    ]
