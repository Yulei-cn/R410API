from django.db import models

class Commentaire(models.Model):
    titre = models.CharField(max_length=100)
    commentaire = models.TextField()
    date_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def __repr__(self):
        return f'<Commentaire: {self.titre}>'
