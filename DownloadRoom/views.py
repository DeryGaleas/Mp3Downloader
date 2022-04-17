from django.shortcuts import render, redirect
import youtube_dl

def download_trigger(request):
    if request.method == 'POST':
        link = request.POST['youtube_link']
        print(link)

        video_url = link
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))

        return redirect('DownloadRoom')
    return render(request, "index.html")

