# Generated by Django 3.0.3 on 2020-02-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gmail', models.EmailField(max_length=254)),
                ('Linkdin', models.EmailField(max_length=254)),
                ('Yahoo', models.EmailField(max_length=254)),
                ('landline', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('mobile2', models.IntegerField()),
            ],
        ),
    ]