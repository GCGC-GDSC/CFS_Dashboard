# Generated by Django 3.2.8 on 2022-02-05 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name',
                 models.CharField(default=None, max_length=30, unique=True)),
                ('inst_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name',
                 models.CharField(default=None, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=10)),
                ('stream',
                 models.ForeignKey(default=None,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='organization.stream')),
                ('under_campus',
                 models.ForeignKey(default=None,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='organization.campus')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('course', models.CharField(default=None, max_length=10)),
                ('is_ug', models.BooleanField(default=True)),
                ('campus',
                 models.ForeignKey(default=None,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='organization.campus')),
                ('institute',
                 models.ForeignKey(default=None,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='organization.institute')),
            ],
        ),
    ]
