# Generated by Django 2.2.12 on 2020-06-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawlingdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Period', models.CharField(max_length=50)),
            ],
        ),
    ]
