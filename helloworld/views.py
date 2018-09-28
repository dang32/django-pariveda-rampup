# helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from imgurpython import ImgurClient
import random

client_id = '5b5458d0a4210d4'
client_secret = '6a411a471c44c607986d477e6fd7676b8702ba04'

client = ImgurClient(client_id, client_secret)

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context_instance=None)

class ImgurPageView(TemplateView):
    def get(self, request, **kwargs):
        # get first page of images from reddit.com/r/aww within the last week
        items = client.subreddit_gallery('aww', sort='time', window='week', page=0)
        #select a random image
        random_image = random.choice(items)
        context = {
            'random_image': random_image
        }
        return render(request, 'imgur.html', context)
