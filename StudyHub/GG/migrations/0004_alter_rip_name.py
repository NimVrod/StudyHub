# Generated by Django 4.0.2 on 2022-05-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GG', '0003_alter_rip_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rip',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
