# Generated by Django 4.0.4 on 2022-05-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clicker', '0004_rename_level_userdata_tentacle1_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tentacles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tentacle1', models.IntegerField(default=0)),
                ('tentacle2', models.IntegerField(default=0)),
                ('tentacle3', models.IntegerField(default=0)),
                ('tentacle4', models.IntegerField(default=0)),
                ('tentacle5', models.IntegerField(default=0)),
            ],
        ),
    ]
