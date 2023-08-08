# Generated by Django 4.2.4 on 2023-08-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_tracking', '0003_devicelog_delete_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelog',
            name='condition_when_returned',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
