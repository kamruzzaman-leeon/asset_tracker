# Generated by Django 4.2.4 on 2023-08-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='condition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
