# Generated by Django 4.1.4 on 2024-04-21 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abadi', '0022_transactionlog_konversimaster_lastedited'),
    ]

    operations = [
        migrations.CreateModel(
            name='confirmationorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoCO', models.CharField(max_length=50)),
                ('kepada', models.CharField(max_length=100)),
                ('perihal', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='detailconfirmationorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskripsi', models.CharField(max_length=200)),
                ('kuantitas', models.IntegerField()),
                ('Harga', models.FloatField()),
                ('Artikel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.artikel')),
                ('confirmationorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abadi.confirmationorder')),
            ],
        ),
    ]
