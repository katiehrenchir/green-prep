# Generated by Django 2.1.7 on 2019-04-14 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0023_auto_20190401_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 18, 21, 52, 127215, tzinfo=utc)),
        ),
    ]
