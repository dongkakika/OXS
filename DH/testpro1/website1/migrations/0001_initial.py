# Generated by Django 3.0.5 on 2020-05-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('userpw', models.CharField(max_length=20)),
            ],
        ),
    ]