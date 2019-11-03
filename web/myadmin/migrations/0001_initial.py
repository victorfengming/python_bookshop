# Generated by Django 2.2.3 on 2019-10-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=80)),
                ('face', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('homeaddress', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=1, null=True)),
                ('usertype', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
