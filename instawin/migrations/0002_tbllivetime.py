# Generated by Django 3.1.3 on 2021-02-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instawin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblLiveTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timed', models.TimeField(max_length=150)),
            ],
        ),
    ]
