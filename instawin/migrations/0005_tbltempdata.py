# Generated by Django 3.1.3 on 2021-02-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instawin', '0004_tblagameone'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbltempdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameId', models.CharField(max_length=600)),
                ('User1', models.CharField(max_length=600)),
                ('User2', models.CharField(max_length=600)),
                ('Amount1', models.CharField(max_length=600)),
                ('Amount2', models.CharField(max_length=600)),
                ('Tamount', models.CharField(max_length=600)),
            ],
        ),
    ]
