# Generated by Django 3.1 on 2020-09-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, unique=True)),
                ('link', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]