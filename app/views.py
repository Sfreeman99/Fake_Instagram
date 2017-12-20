from django.shortcuts import render, redirect
from django.views import View
from app.models import *
from app.forms import *


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
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            ImageModel(name=name, image=image).save()

            return redirect('app:feed')
        else:
            return render(request, 'app/post_photo.html', {'form': form})