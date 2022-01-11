# Generated by Django 4.0.1 on 2022-01-11 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(max_length=124)),
                ('species', models.CharField(default='non-human', max_length=124)),
                ('number_of_apendages', models.IntegerField(default=None)),
                ('number_of_eyes', models.IntegerField(default=None)),
                ('description', models.TextField(default='', max_length=500)),
                ('risk_level', models.IntegerField(default=0)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
