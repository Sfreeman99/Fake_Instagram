from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from app.models import *
from app.forms import *
from app.core import add_overlay
from PIL import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404


# Create your views here.
class SignUp(View):
    def get(self, request):
        return render(request, "app/signup.html", {'form': UserCreationForm()})

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('app:feed')
        else:
            return render(request, 'app/signup.html', {'form': form})


class LogIn(View):
    def get(self, request):
        return render(request, 'app/login.html', {'form': LogInForm})

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('app:feed')
        else:
            return render(request, 'app/login.html', {'form': form})


class LogOut(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('app:signup')


class Feed(LoginRequiredMixin, View):
    login_url = "/signup"
    redirect_field_name = "app:signup"

    def get(self, request):
        return render(request, 'app/feed.html', {
            'images': ImageModel.objects.all()
        })


class CommentView(LoginRequiredMixin, View):
    login_url = "/signup"
    redirect_field_name = "app:signup"

    def get(self, request, id):
        return render(
            request,
            "app/comment-form.html", {
                'form': CommentForm(),
                'photo': ImageModel.objects.get(id=id),
            })

    def post(self, request, id):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            new_comment = CommentModel(
                comment=comment,
                image=ImageModel.objects.get(id=id),
                commentor=request.user.profile).save()
            return redirect("app:feed")
        else:
            render(
                request,
                'app/comment-form.html', {
                    'form': form,
                    'photo': ImageModel.objects.get(id=id),
                })


class PostPhotoView(LoginRequiredMixin, View):
    login_url = "/signup"
    redirect_field_name = "app:signup"

    def get(self, request):
        return render(request, 'app/post_photo.html', {
            'form': PostPhotoForm()
        })

    def post(self, request):
        form = PostPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user.profile)
            # name = form.cleaned_data['name']
            # image = form.cleaned_data['image']
            # ImageModel(name=name, image=image).save()

            return redirect('app:feed')
        else:
            return render(request, 'app/post_photo.html', {'form': form})


class EditPhotoView(LoginRequiredMixin, View):
    login_url = "/signup"
    redirect_field_name = "app:signup"

    def get(self, request, id):
        image = ImageModel.objects.get(id=id)
        if request.user != image.uploaded_by.user:
            raise Http404("You are not authorized to edit {}'s image".format(
                image.uploaded_by.user.username))
        return render(request, 'app/edit_photo.html', {
            'form': EditPhotoForm(),
            'photo': image,
        })

    def post(self, request, id):
        form = EditPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            path = ImageModel.objects.get(id=id).image
            # picture = Image.open(path)
            overlay = form.cleaned_data['over_lay']
            if overlay == "Base Camp Filter":
                add_overlay(path)
                ImageModel.objects.get(id=id).save()
                return redirect('app:feed')
        else:
            return render(
                request,
                'app/edit_photo.html', {
                    'form': form,
                    'photo': ImageModel.objects.get(id=id)
                })
