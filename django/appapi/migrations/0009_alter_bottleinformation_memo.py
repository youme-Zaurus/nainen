# Generated by Django 4.1.1 on 2022-10-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0008_alter_bottleinformation_id_alter_container_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottleinformation',
            name='memo',
            field=models.TextField(null=True, verbose_name='メモ'),
        ),
    ]