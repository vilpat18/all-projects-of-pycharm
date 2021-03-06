# Generated by Django 3.0.3 on 2020-05-15 10:32

from django.db import migrations, models
import django.db.models.deletion
import imageapp.models


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
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('password', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('confirm_password', models.TextField()),
                ('recovery_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.TextField(verbose_name=imageapp.models.Register)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imageapp.Register')),
            ],
        ),
    ]
