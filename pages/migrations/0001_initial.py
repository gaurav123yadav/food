# Generated by Django 3.2 on 2021-06-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]
