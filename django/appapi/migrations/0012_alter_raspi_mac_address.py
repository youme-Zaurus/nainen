# Generated by Django 4.1.1 on 2022-11-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0011_alter_bottletype_options_alter_raspi_mac_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspi',
            name='mac_address',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]