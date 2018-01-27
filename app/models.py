from django.db import models


class CommentModel(models.Model):
    comment = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey("ImageModel", on_delete=models.CASCADE)


class ImageModel(models.Model):
    name = models.CharField(max_length=15, )
    image = models.ImageField(upload_to='./app/static/pictures')

    def image_url(self):
        #return self.image.name[len('app/static/'):]
        return self.original_url()

    def original_url(self):
        return self.image.name[len('app/static/'):]
