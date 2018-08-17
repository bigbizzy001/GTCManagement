# Generated by Django 2.0.4 on 2018-05-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GCTM', '0002_auto_20180518_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
