from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
import youtube_dl

# Create your views here.
class VideoProcessor(View):
    def __init__(self,url=None):
        self.url = url

    def get(self,request):
        return render(request,'app/home.html')

    def post(self,request):
        url = request.POST["given_url"]
        with youtube_dl.YoutubeDL() as ydl:
            url = ydl.extract_info(url, download=False)
            download_link = url["formats"]
            context = {'vids': download_link,'title':url['title']}
            return render(request, 'app/download.html', context)


def features(request):
    return render(request, 'app/features.html')


def contact(request):
    return render(request, 'app/contact.html')