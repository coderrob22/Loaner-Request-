# Generated by Django 4.2.6 on 2023-11-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
