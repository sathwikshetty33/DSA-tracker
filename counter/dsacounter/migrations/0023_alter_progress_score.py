# Generated by Django 5.1.1 on 2024-11-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsacounter', '0022_progress_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
