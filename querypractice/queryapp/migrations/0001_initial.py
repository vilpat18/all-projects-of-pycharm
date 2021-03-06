# Generated by Django 3.0.3 on 2020-11-04 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=256)),
                ('m_salary', models.IntegerField()),
                ('m_contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.Contact_info')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=256)),
                ('e_salary', models.IntegerField()),
                ('e_contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queryapp.Contact_info')),
            ],
        ),
    ]
