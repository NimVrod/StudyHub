# Generated by Django 4.0.2 on 2022-04-24 15:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0005_quiz_views_alter_quiz_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 24, 15, 49, 49, 822601, tzinfo=utc), verbose_name='date_published'),
        ),
    ]
