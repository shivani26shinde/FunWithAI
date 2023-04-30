from django.db import models

class AudioBlog(models.Model):
    text = models.TextField()
    tempo = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_files/')

    def __str__(self):
        return f"AudioBlog {self.pk}"
