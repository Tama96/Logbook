from django.db import models

class Mhs(models.Model):
    nama_mahasiswa = models.CharField( max_length=255)
    nim = models.CharField( max_length=100)
    fakultas = models.CharField( max_length=100)
    jurusan = models.CharField( max_length=100)
    tema_laporan = models.CharField( max_length=250)
    dosen_pembimbing = models.CharField( max_length=250)
