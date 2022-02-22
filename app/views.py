from urllib import request
from django.shortcuts import render, redirect
from pytube import YouTube
from django.views.generic import View

# Create your views here.
class VideoProcessor(View):
    def __init__(self,url=None):
        self.url = url

    def get(self,request):
        return render(request,'app/main.html')    

    def post(self,request):
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            vidTitle,vidThumbnail = video.title,video.thumbnail_url
            stream = []
            for vid in video.streams.filter(progressive=True):
                stream.append(vid)
            context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                        'stream':stream,'url':self.url}
            return render(request,'app/main.html',context)
        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            fetched_video = YouTube(self.url)
            video = fetched_video.streams[int(request.POST.get('download-vid')) - 1]
            video.download(output_path='DownloadedVideos')
            return recirect('download-video')
        return render(request,'app/main.html')


def DownloadVideo(request):
    context = {'vidName': 'How to Deploy a Django App to Heroku The Right Way.3gpp'}
    return render(request, 'app/downloadPage.html', context)