# Generated by Django 4.1.7 on 2023-03-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sins', '0003_alter_guru_nip_alter_siswa_nis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guru',
            name='tgl_lahir',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='tgl_lahir',
            field=models.DateField(),
        ),
    ]
