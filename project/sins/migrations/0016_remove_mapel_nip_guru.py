# Generated by Django 4.1.7 on 2023-04-04 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sins', '0015_mapel_nip_guru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapel',
            name='nip_guru',
        ),
    ]
