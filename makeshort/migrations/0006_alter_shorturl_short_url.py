# Generated by Django 3.2.8 on 2021-10-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeshort', '0005_shorturl_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(blank=True, max_length=6, unique=True),
        ),
    ]
