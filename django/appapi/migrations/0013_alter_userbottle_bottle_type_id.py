# Generated by Django 4.1.1 on 2022-11-06 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0012_alter_raspi_mac_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbottle',
            name='bottle_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='appapi.bottletype', verbose_name='種類ID'),
        ),
    ]