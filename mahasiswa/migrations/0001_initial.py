# Generated by Django 2.0 on 2020-09-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mhs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_mahasiswa', models.CharField(max_length=255)),
                ('nim', models.CharField(max_length=100)),
                ('fakultas', models.CharField(max_length=100)),
                ('jurusan', models.CharField(max_length=100)),
                ('tema_laporan', models.CharField(max_length=250)),
                ('dosen_pembimbing', models.CharField(max_length=250)),
            ],
        ),
    ]
