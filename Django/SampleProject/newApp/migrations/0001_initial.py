# Generated by Django 3.1.7 on 2021-03-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=20)),
                ('vpwd', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
    ]