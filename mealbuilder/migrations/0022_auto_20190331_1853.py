# Generated by Django 2.1.7 on 2019-03-31 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0021_auto_20190331_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 18, 53, 41, 680986, tzinfo=utc)),
        ),
    ]
