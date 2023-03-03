# Generated by Django 4.1.7 on 2023-03-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlevelperm', '0002_user_created_gps_user_device_id_user_firebase_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': ()},
        ),
        migrations.AlterField(
            model_name='user',
            name='device_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]
