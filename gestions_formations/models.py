from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Cour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(("Nom du formateur"), max_length=50)
    prix = models.CharField(("Prix de la formation"), max_length=50)
    nombre_participants = models.IntegerField(
        ("Le nombre de personne ayant suivis la formation"))
    objectif = models.TextField(("Objectifs de la formation"))
    critere = models.TextField(
        ("Represente les criteres pour etre apte a suivre la formation"))
    url = models.URLField(
        ("Ici tu renseigne l'url de ton cour sur podia"), max_length=800)
    url_video_presentation = models.URLField(
        ("Ici tu renseigne l'url de la video de presentation du cour"), max_length=800)
    image = models.ImageField(
        ("Image de presentation de la formation"), upload_to=None)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Cour'
        verbose_name_plural = 'Cours'


class Url_Cour(models.Model):
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE)
    url = models.URLField(
        ("Ici tu renseigne l'url de ton cour sur podia"), max_length=500)
    is_use = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.url
    class Meta:
        verbose_name = 'Url Cour'
        verbose_name_plural = 'Url Cours'