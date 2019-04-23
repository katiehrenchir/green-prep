# Generated by Django 2.1.7 on 2019-03-31 00:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0014_auto_20190330_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealitem',
            old_name='food_item',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='mealitem',
            old_name='food_portion',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='mealitem',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='carbs',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='fat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='protein',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 0, 15, 59, 746790, tzinfo=utc)),
        ),
    ]