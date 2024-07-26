from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from pathlib import Path
from django.core.files import File
from django.contrib.auth.models import Group

class User(AbstractUser):
    class UserRole(models.TextChoices):
        CREATOR = 'CREATOR', 'CREATEUR'
        SUBSCRIBER = 'SUBSCRIBER', 'Abonné'

    def get_default_avatar():
        avatar_path = Path(settings.BASE_DIR.joinpath('static/Images/default_avatar.png'))
        with open(avatar_path, 'rb') as f:
            return File(f)

    photo_profil = models.ImageField(upload_to = 'photo_de_profil_utilisateur/', verbose_name = 'Photo de profil',  blank=True)
    role = models.CharField(choices=UserRole.choices, max_length = 30 ,verbose_name = 'Rôle')
    follows = models.ManyToManyField(
        'self',
        limit_choices_to = {'role': 'CREATOR'},
        symmetrical = False,
        verbose_name = 'suit',
        blank=True,
        related_name='followers'
    )

    def save(self, *args, **kwargs):
        # Appeller la méthode parente
        super().save(*args, **kwargs)
        
        # Faire en sorte que l'utilisateur ne fasse partie d'aucun groupe avant de l'ajouter au groupe
        self.groups.clear()

        # Ajouter l'utilisateur au groupe correspondant ou créer ce dernier
        if self.role == User.UserRole.CREATOR:
            group, created = Group.objects.get_or_create(name='creators')
            gRoup, cReated = Group.objects.get_or_create(name='Creators')
            self.groups.add(group)
            self.groups.add(gRoup)
        elif self.role == User.UserRole.SUBSCRIBER:
            group, created = Group.objects.get_or_create(name='subscribers')
            gRoup, cReated = Group.objects.get_or_create(name='Subscribers')
            self.groups.add(group)
            self.groups.add(gRoup)
        super().save(*args, **kwargs)
        
                



