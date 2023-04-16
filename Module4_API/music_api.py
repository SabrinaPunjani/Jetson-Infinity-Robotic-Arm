#created on 2023-04-16 author @sabrina
# MIT Standard License 
##############################################
##############################################
#
#Problem/Challenge:
#Import songs from youtube and make the Robot dance to them
#
# requirements: 
#               pip install youtube_search
#               pip install python_vlc
#               pip install pafy
#               pip install youtube-dl
#               instalation of 64 bit (32 will not work) version of VLC https://get.videolan.org/vlc/3.0.11/win64/vlc-3.0.11-win64.exe
#  
#
#---------------importing modules-----------------------

import xarm #robotic arm module
import time 
from youtube_search import YoutubeSearch
import pafy
import vlc

#------------initializing variables--------------------------
#arm = xarm.Controller('USB')
PAFY_BACKEND = "internal"

#--------------functions------------------------------------

#play the URL in VLC
def playURL(playurl):
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()




#--------------------main-------------------------------------


song_name = 'succducc - me & u'
results = YoutubeSearch(song_name, max_results=10).to_dict() #put results in a dictionary

v = results.pop(0) #pop the first result from the result list
url = ('https://www.youtube.com' + v['url_suffix'])

video = pafy.new(url) #create pafty instance of our url
audio= video.getbestaudio() #return highest res audio our provided youtube url
playurl = audio.url #url for best audio

playURL(playurl) #play audio with function defined above


