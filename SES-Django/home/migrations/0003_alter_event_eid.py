# Generated by Django 3.2.7 on 2021-09-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210910_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
