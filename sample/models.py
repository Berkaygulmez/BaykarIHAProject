from django.db import models

# Create your models here.

class Sample(models.Model):
    marka = models.CharField(max_length=100)     # Marka adını tutan karakter alanı (en fazla 100 karakter)   
    model = models.CharField(max_length=100)     # model adını tutan karakter alanı (en fazla 100 karakter)
    agirlik = models.CharField(max_length=10)     # ağırlık adını tutan karakter alanı (en fazla 100 karakter)
    kategori = models.CharField(max_length=100)     # kategori adını tutan karakter alanı (en fazla 100 karakter)
    image = models.ImageField(null=True, blank=True, upload_to='sample') #Resmi tutan dosya alanı, null ve boş bırakılabilir

# Nesnenin metinsel temsilini döndüren metod
    def __str__(self):
        return self.marka