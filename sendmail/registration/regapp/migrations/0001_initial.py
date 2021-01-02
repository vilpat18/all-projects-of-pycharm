# Generated by Django 3.0.3 on 2020-04-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=8)),
                ('password2', models.CharField(max_length=8)),
                ('mobile', models.IntegerField(unique=True)),
                ('recovery_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]