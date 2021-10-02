# Generated by Django 3.2.7 on 2021-09-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
