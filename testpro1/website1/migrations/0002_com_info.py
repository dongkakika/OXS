# Generated by Django 3.0.7 on 2020-06-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='com_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Date', models.CharField(max_length=15)),
                ('View', models.CharField(max_length=30)),
                ('Href', models.CharField(max_length=300)),
            ],
        ),
    ]
