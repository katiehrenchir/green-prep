# Generated by Django 2.1.7 on 2019-03-31 04:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0018_auto_20190331_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 4, 49, 0, 517808, tzinfo=utc)),
        ),
    ]