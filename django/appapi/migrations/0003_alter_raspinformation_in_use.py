# Generated by Django 4.1.1 on 2022-10-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0002_alter_user_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspinformation',
            name='in_use',
            field=models.BooleanField(default=1),
        ),
    ]
