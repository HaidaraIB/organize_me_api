# Generated by Django 5.0.4 on 2024-05-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_telecombill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_el_bill',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='last_tel_bill',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='last_wa_bill',
            field=models.IntegerField(default=1),
        ),
    ]
