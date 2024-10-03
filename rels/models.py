from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=250, verbose_name='Заголовок')
    video = models.FileField(
        upload_to='video', 
        verbose_name='Видео',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])]
    )
    like_count = models.BigIntegerField(default=0, null=True, blank=True, verbose_name='Like')

    def add_like(self):
        """Video ga like qo'shish."""
        self.like_count += 1  # Like hisobini oshirish
        self.save()  # O'zgarishlarni saqlash

    def __str__(self):
        return self.name

    class Meta:
        db_table = "video"
        verbose_name = "Видео"
        verbose_name_plural = "Видео"