# Generated by Django 4.1 on 2023-02-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0006_alter_kebele_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kebele',
            name='id',
            field=models.IntegerField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
