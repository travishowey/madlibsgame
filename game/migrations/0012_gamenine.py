# Generated by Django 2.2 on 2022-03-07 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_gameeight'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameNine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('setting', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('problem', models.CharField(max_length=200)),
                ('adjective', models.CharField(max_length=200)),
                ('adjectiveTwo', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=200)),
            ],
        ),
    ]
