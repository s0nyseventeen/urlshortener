# Generated by Django 3.2.8 on 2021-10-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeshort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(default='admindefault', max_length=255),
            preserve_default=False,
        ),
    ]
