from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from app.models import *
from app.forms import *
from app.core import add_overlay
from PIL import Image
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class SignUp(View):
    def get(self, request):
        return render(request, "app/signup.html", {'form': SignUpForm()})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user if the form is valid
            user.refresh_from_db(
            )  # Load user information created by the signal in the Model
            user.profile.birth_date = form.cleaned_data[
                'birth_date']  # Goes in the users profile information and updates the birthdate
            user.save()  # save the user and update their information
            raw_password = form.cleaned_data['password1']  # get their password
            user = authenticate(
                username=user.username, password=raw_password
            )  # authenticate that this user exists and is valid
            login(
                request,
                user)  # if the authentication was correct, it will log you in
            return redirect('app:feed')
        else:
            form = SignUpForm()
        return render(request, "app/signup.html", {'form': SignUpForm})


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
            CommentModel(
                comment=comment, image=ImageModel.objects.get(id=id)).save()
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
            form.save()
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
