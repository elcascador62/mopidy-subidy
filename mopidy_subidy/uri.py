import re

SONG = 'song'
ARTIST = 'artist'
PLAYLIST = 'playlist'
ALBUM = 'album'
PREFIX = 'subidy'
ROOT = 'root'

ROOT_URI = '%s:%s' % (PREFIX, ROOT)

regex = re.compile(r'(\w+?):(\w+?)(?::|$)(.+?)?$')

def is_type_result_valid(result):
    return result is not None and result.group(1) == PREFIX

def is_id_result_valid(result, type):
    return is_type_result_valid(result) and result.group(1) == PREFIX and result.group(2) == type

def get_song_id(uri):
    result = regex.match(uri)
    if not is_id_result_valid(result, SONG):
        return None
    return result.group(3)

def get_artist_id(uri):
    result = regex.match(uri)
    if not is_id_result_valid(result, ARTIST):
        return None
    return result.group(3)

def get_playlist_id(uri):
    result = regex.match(uri)
    if not is_id_result_valid(result, PLAYLIST):
        return None
    return result.group(3)

def get_album_id(uri):
    result = regex.match(uri)
    if not is_id_result_valid(result, ALBUM):
        return None
    return result.group(3)

def get_type(uri):
    result = regex.match(uri)
    if not is_type_result_valid(result):
        return None
    return result.group(2)

def get_type_uri(type, id):
    return u'%s:%s:%s' % (PREFIX, type, id)

def get_artist_uri(id):
    return get_type_uri(ARTIST, id)

def get_album_uri(id):
    return get_type_uri(ALBUM, id)

def get_song_uri(id):
    return get_type_uri(SONG, id)