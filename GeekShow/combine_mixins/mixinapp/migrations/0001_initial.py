# Generated by Django 3.0.3 on 2020-11-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mumbai', models.CharField(max_length=100)),
                ('Delhi', models.CharField(max_length=100)),
                ('Banglore', models.CharField(max_length=100)),
            ],
        ),
    ]