# Generated by Django 4.0.2 on 2022-05-21 14:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0013_alter_quiz_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 21, 14, 27, 32, 987152, tzinfo=utc), verbose_name='date_published'),
        ),
    ]