
# Generated by Django 2.1.7 on 2019-03-04 18:37


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('calories', models.IntegerField()),
                ('protein', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbs', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('creation_date', models.DateTimeField(default=datetime.datetime(2019, 3, 4, 18, 0, 58, 106377, tzinfo=utc))),

            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
    ]
