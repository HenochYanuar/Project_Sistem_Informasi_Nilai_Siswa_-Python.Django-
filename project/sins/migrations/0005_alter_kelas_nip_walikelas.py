# Generated by Django 4.1.7 on 2023-03-30 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sins', '0004_alter_guru_tgl_lahir_alter_siswa_tgl_lahir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelas',
            name='nip_waliKelas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sins.guru'),
        ),
    ]
