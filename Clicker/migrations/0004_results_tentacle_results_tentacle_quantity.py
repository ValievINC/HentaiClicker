# Generated by Django 4.1.4 on 2023-01-07 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clicker', '0003_tentacles_alter_results_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='tentacle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clicker.tentacles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='tentacle_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]