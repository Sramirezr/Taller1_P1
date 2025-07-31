from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    # Asegúrate de que tu campo 'poster' esté aquí. Por ejemplo:
    poster = models.ImageField(upload_to='movies/posters/', null=True, blank=True) # Lo hago opcional por si acaso

    def __str__(self):
        return self.title