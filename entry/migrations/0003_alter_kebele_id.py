# Generated by Django 4.1 on 2023-02-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_kebele_remove_resident_admin_remove_resident_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kebele',
            name='id',
            field=models.IntegerField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
