# Generated by Django 3.1.3 on 2021-02-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instawin', '0002_tbllivetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblresult1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultt1', models.CharField(blank=True, default=None, max_length=600, null=True)),
            ],
        ),
    ]