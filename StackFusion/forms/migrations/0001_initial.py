# Generated by Django 3.0.4 on 2020-03-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
                ('dateOfBirth', models.DateField(max_length=10)),
            ],
        ),
    ]
