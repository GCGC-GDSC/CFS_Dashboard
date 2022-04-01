# Generated by Django 3.2.8 on 2021-12-25 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCousesPlaced',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('placed', models.IntegerField(default=-1)),
                ('company',
                 models.ForeignKey(default=None,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='company.company')),
                ('courses',
                 models.ForeignKey(default=None,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='company.courses')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='courses',
            field=models.ManyToManyField(through='company.CompanyCousesPlaced',
                                         to='company.Courses'),
        )
    ]