# Generated by Django 4.1.7 on 2023-03-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]