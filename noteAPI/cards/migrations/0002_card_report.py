# Generated by Django 3.0.7 on 2020-06-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='report',
            field=models.BooleanField(default=False),
        ),
    ]
