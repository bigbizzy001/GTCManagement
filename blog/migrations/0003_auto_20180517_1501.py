# Generated by Django 2.0.4 on 2018-05-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180517_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
