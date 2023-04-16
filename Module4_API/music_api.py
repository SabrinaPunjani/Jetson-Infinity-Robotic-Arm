#created on 2023-04-16 author @sabrina
##############################################
##############################################
#
#Problem/Challenge:
#Import songs from youtube and make the Robot dance to them
#
# module requirements: pip install youtube-search
#
#
#---------------importing modules-----------------------

import xarm #robotic arm module
import time 
from youtube_search import YoutubeSearch
#------------initializing variables--------------------------
#arm = xarm.Controller('USB')


#-----------------------------------------------------------
song_name = 'succducc - me & u'
results = YoutubeSearch(song_name, max_results=10).to_dict()
for v in results:
    print('https://www.youtube.com' + v['url_suffix'])