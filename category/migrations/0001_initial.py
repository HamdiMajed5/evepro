# Generated by Django 4.0.2 on 2022-03-17 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrid', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=60, null=True)),
                ('teacher_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='category.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_mark', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0)),
                ('parent_mark', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], default=0)),
                ('teacher_mark', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('note', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.participant')),
            ],
        ),
        migrations.AddConstraint(
            model_name='evaluation',
            constraint=models.UniqueConstraint(fields=('category', 'participant'), name='participant_already_evaluated'),
        ),
    ]
