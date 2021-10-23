# Generated by Django 3.2.8 on 2021-10-23 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('makeshort', '0002_shorturl_short_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
