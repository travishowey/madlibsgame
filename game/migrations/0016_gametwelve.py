# Generated by Django 2.2 on 2022-03-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_gameeleven'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameTwelve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=200)),
                ('adjectiveWithLy', models.CharField(max_length=200)),
                ('verbTwo', models.CharField(max_length=200)),
                ('bodyPart', models.CharField(max_length=200)),
                ('plants', models.CharField(max_length=200)),
                ('food', models.CharField(max_length=200)),
                ('noun', models.CharField(max_length=200)),
                ('streetName', models.CharField(max_length=200)),
                ('verbWithIng', models.CharField(max_length=200)),
                ('verbWithIngTwo', models.CharField(max_length=200)),
                ('foodTwo', models.CharField(max_length=200)),
            ],
        ),
    ]
