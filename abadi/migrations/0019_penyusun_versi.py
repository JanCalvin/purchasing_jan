# Generated by Django 4.1.4 on 2024-04-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0018_produksubkon_keterangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='penyusun',
            name='versi',
            field=models.DateField(blank=True, null=True),
        ),
    ]
