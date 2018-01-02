from django.db import models

# Create your models here.


class ImageModel(models.Model):
    name = models.CharField(
        max_length=15, )
    image = models.ImageField(
        upload_to='app/static/pictures/', )
    filtered = models.ImageField(
        upload_to='app/static/filtered_pictures/', blank=True)

    def image_url(self):
        #return self.image.name[len('app/static/'):]
        if self.filtered:
            return self.filtered_url()
        else:
            return self.original_url()

    def original_url(self):
        return self.image.name[len('app/static/'):]

    def filtered_url(self):
        return self.filtered.name[len('app/static/')]