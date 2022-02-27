from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
import youtube_dl

# Create your views here.
class VideoProcessor(View):
    def __init__(self,url=None):
        self.url = url

    def get(self,request):
        return render(request,'app/main.html')    

    def post(self,request):
        url = request.POST["given_url"]
        print("Someone just tried to download", url)
        with youtube_dl.YoutubeDL() as ydl:
            url = ydl.extract_info(url, download=False)
            print(url)
            try:
                download_link = url["entries"][-1]["formats"][-1]["url"]
            except:
                download_link = url["formats"][-1]["url"]
            return redirect(download_link+"&dl=1")