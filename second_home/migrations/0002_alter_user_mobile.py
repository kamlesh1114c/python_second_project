# Generated by Django 4.0.6 on 2022-08-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(default=''),
        ),
    ]
