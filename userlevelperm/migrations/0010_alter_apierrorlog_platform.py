# Generated by Django 4.1.5 on 2023-03-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlevelperm', '0009_apierrorlog_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apierrorlog',
            name='platform',
            field=models.PositiveBigIntegerField(choices=[(0, 'Android'), (1, 'Ios')], default=1),
        ),
    ]
