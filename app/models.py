from django.db import models

# Create your models here.


class ImageModel(models.Model):
    name = models.CharField(
        max_length=15, )
    image = models.ImageField(upload_to='./app/static/pictures')

    def image_url(self):
        #return self.image.name[len('app/static/'):]
        return self.original_url()

    def original_url(self):
        return self.image.name[len('app/static/'):]