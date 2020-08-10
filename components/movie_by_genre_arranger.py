import os
from .get_genre import getGenre


def movieGenreArranger(src, des, fname, file_name):
    if not(os.path.exists(des+'video')):
        os.makedirs(des+'video')
    genre = getGenre(fname)
    if(genre != None):
        if (not os.path.exists(des+"video/"+genre)):
            os.makedirs(des+"video/"+genre)
        os.rename(src+file_name, des + "video/"+genre+'/'+file_name)
    else:
        os.rename(src+file_name, des+"video/"+file_name)
