#created on 2023-04-16 author @sabrina
#MIT Open Source Initiative License 
##############################################
##############################################
#
#Problem/Challenge:
#Import songs from youtube and make the Robot dance to them
#
# requirements: 
#               pip install youtube_search
#               pip install python_vlc
#               pip install pytube
#               instalation of 64 bit (32 will not work) version of VLC https://get.videolan.org/vlc/3.0.11/win64/vlc-3.0.11-win64.exe
#              
#
#
#---------------importing modules-----------------------
from __future__ import unicode_literals
import youtube_dl
import xarm #robotic arm module
import time 
from youtube_search import YoutubeSearch
import vlc
from pytube import YouTube

#------------initializing variables--------------------------
#arm = xarm.Controller('USB')
TIME = 40 #seconds song will play

#--------------functions------------------------------------

    
def downloadVideo(url):
    YouTube(url).streams.get_audio_only().download()

    yt = YouTube(url)
    yt.streams
    try:
        yt.filter(progressive=True, file_extension='mp4')
        yt.order_by('resolution')[-1]
        print("downloading")
        yt.download()
    except Exception as E:
        print("already downloaded")
    return (yt.title+'.mp4')


def playAudio(file):
    global TIME
    # creating vlc media player object
    media_player = vlc.MediaPlayer()
    
    # media object
    media = vlc.Media(file)
    
    # setting media to the media player
    media_player.set_media(media)
    
    
    # start playing video
    media_player.play()
    
    #let song play for TIME seconds
    time.sleep(TIME)
 
   
        
    
    
    

#--------------------main-------------------------------------



    
song_name = input("enter song name")
results = YoutubeSearch(song_name, max_results=10).to_dict() #put results in a dictionary

v = results.pop(0) #pop the first result from the result list
url = ('https://www.youtube.com' + v['url_suffix'])

file = downloadVideo(url)


playAudio(file)
