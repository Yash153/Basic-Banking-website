# Generated by Django 3.1.6 on 2021-07-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=100)),
                ('balance', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TransferModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('amount', models.FloatField(max_length=40)),
                ('dt', models.CharField(max_length=50)),
            ],
        ),
    ]
