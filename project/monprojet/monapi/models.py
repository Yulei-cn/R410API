from django.db import models

class Client(models.Model):
    GENRE_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)
    identifiant = models.CharField(max_length=100, unique=True)
    mot_de_passe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    mail = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nom
