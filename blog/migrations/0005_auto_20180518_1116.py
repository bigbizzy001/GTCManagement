# Generated by Django 2.0.4 on 2018-05-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180518_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(auto_now_add=True),
        ),
    ]
