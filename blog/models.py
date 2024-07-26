from django.db import models
from django.conf import settings
from PIL import Image

class Photo(models.Model):
    image = models.ImageField()
    captions = models.CharField(max_length= 128, blank = True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail = (self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()




class Blog(models.Model):
    photo = models.ForeignKey(Photo, null = True, on_delete=models.SET_NULL, blank = True)
    title = models.CharField(max_length = 128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributors', related_name='contributions') 

    def _get_word_count(self):
        content_count = self.content 
        mots = content_count.split()
        self.word_count = len(mots)

    def save(self, *args, **kwargs):
        self._get_word_count()  # Met à jour le nombre de mots avant de sauvegarder
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.title
        
class BlogContributors(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('blog', 'contributor')



# Create your models here.
