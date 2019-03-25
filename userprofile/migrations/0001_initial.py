# Generated by Django 2.1.7 on 2019-03-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('activity_level', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Lightly Active'), (2, 'Moderately Active'), (3, 'Very Active'), (4, 'Extra Active')], null=True)),
                ('physical_goal', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Fat Loss'), (2, 'Maintenence'), (3, 'Muscle Gain')], null=True)),
                ('p_goal', models.IntegerField()),
                ('c_goal', models.IntegerField()),
                ('f_goal', models.IntegerField()),
            ],
        ),
    ]
