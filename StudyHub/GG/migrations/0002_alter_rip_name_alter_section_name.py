# Generated by Django 4.0.2 on 2022-05-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rip',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]