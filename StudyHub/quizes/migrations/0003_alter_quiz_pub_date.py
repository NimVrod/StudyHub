# Generated by Django 4.0.2 on 2022-02-24 14:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_odpowiedz_is_correct_quiz_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 24, 14, 54, 46, 642249, tzinfo=utc), verbose_name='date_published'),
        ),
    ]
