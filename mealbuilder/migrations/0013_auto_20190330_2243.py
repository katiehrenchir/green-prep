# Generated by Django 2.1.7 on 2019-03-30 22:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0012_auto_20190330_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 22, 43, 5, 656549, tzinfo=utc)),
        ),
    ]