from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=35)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class CommentModel(models.Model):
    comment = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey("ImageModel", on_delete=models.CASCADE)


class ImageModel(models.Model):
    description = models.CharField(max_length=250, )
    image = models.ImageField(upload_to='./app/static/pictures')

    uploaded_by = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True)

    def image_url(self):
        #return self.image.name[len('app/static/'):]
        return self.original_url()

    def original_url(self):
        return self.image.name[len('app/static/'):]
