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
#               pip install tempocnn
#               instalation of 64 bit (32 will not work) version of VLC https://get.videolan.org/vlc/3.0.11/win64/vlc-3.0.11-win64.exe
#              
#
#
#---------------importing modules-----------------------
from __future__ import unicode_literals
import youtube_dl
import xarm #robotic arm module
import time 
import threading
from youtube_search import YoutubeSearch
import vlc
from pytube import YouTube
import librosa
import numpy
import tempocnn
from tempocnn.classifier import TempoClassifier
from tempocnn.feature import read_features
#------------initializing variables--------------------------
arm = xarm.Controller('USB')
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

def dance(file):
    global TIME
    # initialize the model (may be re-used for multiple files)
    classifier = TempoClassifier('model')

    # read the file's features
    features = read_features(file)

    # estimate the global tempo
    tempo = classifier.estimate_tempo(features, interpolate=False)
    # map beat to arm movements
    for i in range(TIME):
        if i % 2 == 0:
            arm.set_position([3,270], [5, 715])
            
        else:
            arm.set_position([3,750], [5, 415])
            
        time.sleep(60 / tempo)
        
        
def playAudio(file):
    global TIME
    # creating vlc media player object
    media_player = vlc.MediaPlayer()
    
    # media object
    media = vlc.Media(file)
    
    # setting media to the media player
    media_player.set_media(media)
    def playmusic():
        print("play")
        
       
        
    song_thread = threading.Thread(target=playmusic, args=([]))
    song_thread.daemon = True
    dance_thread = threading.Thread(target=dance, args=([file]))
    dance_thread.daemon = True 
    # start playing 
    #song_thread.start()
    #start dancing
    dance_thread.start()
    media_player.play()
        
    time.sleep(TIME)#let song play for TIME seconds
    
   
    
    
    
 

        

        
    

#--------------------main-------------------------------------



    
song_name = input("enter song name")
results = YoutubeSearch(song_name, max_results=10).to_dict() #put results in a dictionary

v = results.pop(0) #pop the first result from the result list
url = ('https://www.youtube.com' + v['url_suffix'])

file = downloadVideo(url)


playAudio(file)
