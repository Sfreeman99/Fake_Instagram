from django.shortcuts import render
from django.views import View


# Create your views here.
class Feed(View):
    def get(request):
        return render(request, 'templates/feed.html', {'form': FeedForm()})