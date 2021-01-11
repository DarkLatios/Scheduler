# Generated by Django 3.0.5 on 2021-01-11 20:14

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_remove_hall_floors'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='floors',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), default=12, max_length=66, size=6),
            preserve_default=False,
        ),
    ]
