# Generated by Django 3.0.5 on 2021-01-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210110_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='condition',
            name='time',
            field=models.TimeField(),
        ),
    ]