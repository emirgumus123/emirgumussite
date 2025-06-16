from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider/')
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderlar'
        ordering = ['order']

class Haberler(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='haberler/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'
        ordering = ['-created_at']  # En son eklenen haberler en üstte görünsün

class Hizmetler(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hizmetler/')
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Adı")
    email = models.EmailField(verbose_name="E-posta")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


@receiver(post_delete)
def delete_file_on_model_delete(sender, instance, **kwargs):
    for field in instance._meta.fields:
        if hasattr(field, 'upload_to'):
            file = getattr(instance, field.name)
            if file and hasattr(file, 'path') and os.path.isfile(file.path):
                os.remove(file.path)
