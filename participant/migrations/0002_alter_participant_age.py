# Generated by Django 4.0.2 on 2022-02-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]