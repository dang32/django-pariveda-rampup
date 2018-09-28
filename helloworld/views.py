# helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
import urllib
import json
import omdb

def search_movie(title):
    if len(title) < 1 or title=='quit':
        print("Goodbye now...")
        return None
#    try:
url = "http://www.omdbapi.com/?apikey=81b8f4d5&"
#url = serviceurl + urllib.parse.urlencode({'t': title})+apikey+'&'
print('Retrieving the data of "{title}" now... ')
uh = urllib.urlopen(url)
data = uh.read()
context = {'movie_list': json.loads(data)}
context = {'movie_list': ['2','hey','test']}

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context_instance=None)

class TwitterPageView(TemplateView):

#    if json_data['Response']=='True':
#         print_json(json_data)
#    except urllib.error.URLError as e:
#        print("ERROR: {e.reason}")
    def get(self, request, **kwargs):
        return render(request, 'twitter.html', context)
