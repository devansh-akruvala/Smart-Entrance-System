# Generated by Django 3.2.7 on 2021-09-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_event_eid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=100, null=True)),
                ('attendees_name', models.CharField(max_length=50, null=True)),
                ('attendees_email', models.CharField(max_length=50, null=True)),
                ('attendees_phone', models.IntegerField(max_length=10, null=True)),
                ('age', models.IntegerField(max_length=3, null=True)),
            ],
        ),
    ]
