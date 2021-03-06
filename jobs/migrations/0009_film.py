# Generated by Django 3.0.5 on 2021-01-11 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_delete_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(blank=True, max_length=200)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='jobs.Hall')),
            ],
        ),
    ]
