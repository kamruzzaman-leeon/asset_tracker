# Generated by Django 4.2.4 on 2023-08-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_tracking', '0008_alter_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]