# Generated by Django 3.2.8 on 2021-10-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeshort', '0003_shorturl_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
