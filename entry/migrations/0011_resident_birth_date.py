# Generated by Django 4.1 on 2023-02-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0010_remove_resident_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='birth_date',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
