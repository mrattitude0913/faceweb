# Generated by Django 2.1.7 on 2021-04-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_profileing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('c_password', models.CharField(max_length=30)),
            ],
        ),
    ]
