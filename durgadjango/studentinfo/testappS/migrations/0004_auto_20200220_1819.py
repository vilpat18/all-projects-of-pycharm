# Generated by Django 3.0.3 on 2020-02-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testappS', '0003_auto_20200220_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.IntegerField(max_length=11),
        ),
    ]