# Generated by Django 4.1.1 on 2022-11-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0013_alter_userbottle_bottle_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbottle',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='メモ'),
        ),
    ]