# Generated by Django 4.2.4 on 2023-08-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_tracking', '0004_alter_devicelog_condition_when_returned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='condition',
            field=models.CharField(blank=True, choices=[('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')], max_length=10, null=True),
        ),
    ]
