# Generated by Django 2.2 on 2022-03-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_gametwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personOne', models.CharField(max_length=200)),
                ('personTwo', models.CharField(max_length=200)),
                ('bread', models.CharField(max_length=200)),
                ('noun', models.CharField(max_length=200)),
                ('nounTwo', models.CharField(max_length=200)),
                ('nounThree', models.CharField(max_length=200)),
                ('adjective', models.CharField(max_length=200)),
            ],
        ),
    ]
