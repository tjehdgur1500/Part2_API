# Generated by Django 3.0.7 on 2020-06-14 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=60)),
                ('cardInfo', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]
