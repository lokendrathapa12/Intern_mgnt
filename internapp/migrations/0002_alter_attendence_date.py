# Generated by Django 3.2.12 on 2022-06-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.DateField(default=' '),
        ),
    ]
