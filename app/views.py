from django.shortcuts import render, redirect
from django.views import View
from app.models import *
from app.forms import *
from app.core import add_overlay
from PIL import Image


# Create your views here.
class Feed(View):
    def get(self, request):
        return render(request, 'app/feed.html',
                      {'images': ImageModel.objects.all()})


class PostPhotoView(View):
    def get(self, request):
        return render(request, 'app/post_photo.html',
                      {'form': PostPhotoForm()})

    def post(self, request):
        form = PostPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # image = form.cleaned_data['image']
            # ImageModel(name=name, image=image).save()

            return redirect('app:feed')
        else:
            return render(request, 'app/post_photo.html', {'form': form})


class EditPhotoView(View):
    def get(self, request, id):
        return render(
            request,
            'app/edit_photo.html', {
                'form': EditPhotoForm(),
                'photo': ImageModel.objects.get(id=id),
            })

    def post(self, request, id):
        form = EditPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            path = ImageModel.objects.get(id=id).image
            picture = Image.open(path)
            overlay = form.cleaned_data['over_lay']
            filtered_image = add_overlay(path, overlay)
            return redirect('app:feed')
        else:
            return render(
                request,
                'app/edit_photo.html',
                {'form': form,
                 'photo': ImageModel.objects.get(id=id)})
