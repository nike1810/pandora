#-*- coding: utf-8 -*-
# http://habrahabr.ru/post/178215/
from __future__ import division
import requests as r
import BeautifulSoup as bs
import re
import os
import urllib
import urllib2
import json
from crypto import Crypto
import time

TITLE_PATT = re.compile(">(.*?)<")
SAMPLE_PATT = re.compile("http\S*3")
COMPARE_PATT = re.compile("\/[^\/]*.mp3")

#https://oauth.vk.com/authorize?client_id=3665077&scope=audio&redirect_uri=https://oauth.vk.com/blank&display=wap&response_type=token

COOKIE = 'at=wR3JtOkD5uML+hpRZts7J9nGAfao51kP9+mWXzdt95pb2iuYxCrLqMlU3pJwmIYf5POmKDqWEOoNNtwtzqvlH7A%3D%3D'
CONFIG_URL = 'https://gist.github.com/ustasb/596f1ee96d03463fde77/raw/pandata_config.json'
ACCESS_TOKEN = "f089ff91fdec3c8b01ba642cbf918fb8cbb705fccb0c15799c629a31d149f7f45866a32d63d792b78d4d5"
COUNT_OF_SONGS = 1
COUNT_OF_DUPLICATES = 3
DOWNLOAD_FOLDER_NAME = "audio"
LOGIN = "demidov.1810"
PARTNER_LOGIN = 'android'
PARTNER_PASSWORD = 'AC7IBG09A3DTSYM4R41UJWL07VLN8JI7'
USER_NAME = 'demidov.1810@gmail.com'
USER_PASSWORD = 'demon1810'
IN_KEY = 'R=U!LH$O2B#'
OUT_KEY = '6#26FRL$ZWD'
DEVICE = 'android-generic'
RPC_HOST = "tuner.pandora.com"
ONE_HOST = "internal-tuner.pandora.com"
RPC_PATH = "/services/json/?"
HTTP_TIMEOUT = 30

VK_GRANDTYPE = "password"
VK_APPID = "3665077"
VK_SECRETKEY = "cwrhrpcPfkIydbWgH8xc"
VK_USERNAME = "nike.net@mail.ru"
VK_PASSWORD = "baron1810"

# def get_names(n = COUNT_OF_SONGS):
#     l = 1000
#     i = 1
#     out = []
#     count = 1
#
#     cookies = get_cookies()
#
#     while l>100:
#         if not n is None:
#             if i >= n:
#                 break
#
#         resp = r.get("http://www.pandora.com/content/tracklikes?likeStartIndex=0&thumbStartIndex="+str(count)+"&webname="+LOGIN,
#                              headers = {"Cookie": cookies})
#         soup = bs.BeautifulSoup(resp.text)
#         print soup
#
#         for x in soup.findAll(attrs={"class":"infobox-body"}):
#             patt = [PATT.findall(str(x.a))[0], PATT.findall(str(x.p.a))[0]]
#             if patt not in out:
#                 out.append([PATT.findall(str(x.a))[0], PATT.findall(str(x.p.a))[0]])
#             i += 1
#
#         if not "infobox-body" in resp.text and not "no_more tracklike" in resp.text:
#             print "Something bad. Check your cookie"
#             exit()
#
#         l = len(resp.text)
#         count += 1
#
#     # print len(out)
#     # print out
#     return out
#
# def get_cookies():
#     response = r.get(CONFIG_URL)
#     cookies = json.loads(response.text)
#
#     return cookies["cookie"]
#
# def get_vktoken():
#     return ACCESS_TOKEN
# #
# #     string = "https://oauth.vk.com/token?grant_type=password&client_id=%(client_id)s&client_secret=%(secret_key)s&username=%(username)s&password=%(password)s&scope=offline" %{"client_id" : VK_APPID, "secret_key" : VK_SECRETKEY, "username" : VK_USERNAME, "password" : VK_PASSWORD }
# #     print string
# #     resp = r.get(string)
# #     print "get_vktoken after"
# #     print resp.json()
#
#
# def audio_search(string):
#     accessToken = get_vktoken()
#     resp = r.get("https://api.vk.com/method/audio.search?q=%(q)s&sort=2&count=30&access_token=%(ACCESS_TOKEN)s"%{"q":string, "ACCESS_TOKEN":accessToken})
#     return resp.json()
#
# def fillObjectsInfo(objects):
#     i = 1
#     fillingObjects = {}
#
#     while not objects[i] is None :
#         if i > 10:
#             break
#             # print objects[i]
#         head = r.head(objects[i]["url"])
#         size = head.headers["content-length"]
#         duration = objects[i]["duration"]
#         bytrate = (float(size) * 8 / float(duration)) / 1024
#         if bytrate > 300:
#             fillingObjects[bytrate] = objects[i]
#         i+=1
#
#     return fillingObjects
#
# def sortObjects(objects):
#     sortedObjects = []
#     count = 0
#     copies = COUNT_OF_DUPLICATES
#     for key in sorted(objects.keys(), reverse=True):
#         if count >= copies:
#             break
#         sortedObjects.append(objects[key])
#         count+=1
#
#     return sortedObjects
#
# def download(folder=DOWNLOAD_FOLDER_NAME):
#     if not os.path.exists(folder):
#         os.mkdir(folder)
#     for song in get_names():
#         if len(song) == 1:
#             song.append("Unknown")
#         try:
#             originalSongName = song[0]+" "+song[1]
#             get_vktoken()
#             objects = audio_search(originalSongName)["response"]
#             print objects
#             unsortedObject = fillObjectsInfo(objects)
#
#         except:
#             continue
#
#         sortedObjects = sortObjects(unsortedObject)
#         print sortedObjects
#
#
#         for obj in sortedObjects:
#             print "start to download", obj["title"] + "-"+obj["artist"]
#             try:
#                 songPath = os.path.join(folder, originalSongName)
#                 if not os.path.exists(songPath):
#                     os.mkdir(songPath)
#
#                 urllib.urlretrieve(obj["url"], os.path.join(songPath,  obj["title"] + "-"+obj["artist"] +".mp3"))
#             except:
#                 print 'Download fault'
#                 continue
#             print obj["title"] + "-"+obj["artist"], "downloaded"
#
#
#
#
# download()



# ------------------------------------------------------------------------------------------------------------------
class PandoraSong:
    def __init__(self):
        self.artist = ""
        self.title = ""
        self.sample = ""
class Song:
    def __init__(self):
        self.artist = ""
        self.title= ""
        self.duration = 0
        self.bitrate = 0
        self.url =  ""
        self.size = 0

class Pandora:
    def __init__(self):
        self.getCookie()
        self.login = LOGIN

    def getCookie(self):
        response = r.get(CONFIG_URL)
        self.cookie =json.loads(response.text)["cookie"]

    def getLikedTracks(self, countOfSongs = 100):
        l = 1000
        artistNames = []
        sampleSongs = []
        compareSampleSongs = []
        namesAndSamples = []
        count = 1

        while l>100:
            if not countOfSongs is None:
                if len(artistNames) >= countOfSongs:
                    break

            resp = r.get("http://www.pandora.com/content/tracklikes?likeStartIndex=0&thumbStartIndex="+str(count)+"&webname="+self.login,
                                 headers = {"Cookie": self.cookie})
            soup = bs.BeautifulSoup(resp.text)
            # print soup
            for x in soup.findAll(attrs={"class":"infobox-body"}):
                patt = [TITLE_PATT.findall(str(x.a))[0], TITLE_PATT.findall(str(x.p.a))[0]]
                if patt not in artistNames:
                    artistNames.append([TITLE_PATT.findall(str(x.a))[0], TITLE_PATT.findall(str(x.p.a))[0]])
                    # nameCounter += 1

            for sampleStr in soup.findAll(attrs={"class" : "int-icon-1 i-play-1 sample"}):
                sample = re.findall(SAMPLE_PATT, str(sampleStr))
                compare = re.findall(COMPARE_PATT, str(sample))
                if compare not in compareSampleSongs:
                    compareSampleSongs.append(compare)
                    sampleSongs.append(sample)



            if not "infobox-body" in resp.text and not "no_more tracklike" in resp.text:
                print "Something bad. Check your cookie"
                exit()

            l = len(resp.text)
            count += 1

        if(len(artistNames) != len(sampleSongs)):
            print "Mismatch count of songs: %s & artist: %s" % (len(sampleSongs), len(artistNames))
            exit()

        bufCounter = 0
        for artist in artistNames:
            namesAndSamples.append([artist, sampleSongs[bufCounter]])
            bufCounter+=1


        # print "Count of songs: %s & artist: %s" % (len(sampleSongs), len(artistNames))
        #
        # [ namesAndSamples.append( [artist, sample] ) for artist in artistNames for sample in sampleSongs]

        # print "Count of namesAndSamples: %s" % (len(namesAndSamples))

        # print len(out)
        print namesAndSamples
        # print artistNames
        return artistNames

class VKcom:
    def __init__(self):
        self.getToken()

    def getToken(self):
        self.accessToken = ACCESS_TOKEN

    def audioSearch(self, songName):
        resp = r.get("https://api.vk.com/method/audio.search?q=%(q)s&sort=2&count=30&access_token=%(ACCESS_TOKEN)s"%{"q":songName, "ACCESS_TOKEN":self.accessToken})
        # print resp.json()
        return resp.json()

class Downloader:
    def __init__(self):
        self.pandora = Pandora()
        self.vk = VKcom()
        self.countItemsPerSong = 10
        self.useFilterBitrate = True
        self.filterBitrate = 300

    def download(self, folder = "audio"):
        if not os.path.exists(folder):
            os.mkdir(folder)

        for song in self.pandora.getLikedTracks():
            if len(song) == 1:
                song.append("Unknown")
            # try:
            originalSongName = song[0]+" "+song[1]
            objects = self.vk.audioSearch(originalSongName)["response"]
            songs = self.getSongsInfo(objects)

            # except:
            #     continue

            if self.useFilterBitrate :
                songs = self.filterSongs(songs)


            # sortedObjects = sortObjects(unsortedObject)
            # print sortedObjects


            for song in songs:
                print "start to download", song.artist + "-"+ song.name
                try:
                    songPath = os.path.join(folder, originalSongName)
                    if not os.path.exists(songPath):
                        os.mkdir(songPath)

                    filename = os.path.join(songPath,  song.artist + "-"+ song.name +".mp3")
                    if os.path.exists(filename):
                        # print "song local size: %d" % song.size
                        # print "song server size: %d" % os.path.getsize(filename)
                        if os.path.getsize(filename) == song.size:
                            print "File was already downloaded: ", song.artist + "-"+ song.name
                            continue

                    urllib.urlretrieve(song.url, filename)
                    # urllib.urlretrieve(song., os.path.join(songPath,  song.artist + "-"+ song.name +".mp3"))
                except:
                    print 'Download fault'
                    continue
                print song.artist + "-"+ song.name, "downloaded"

    def getSongsInfo(self, objects):
        i = 1
        songs = []
        songsNames = []
        # songsDict = {}

        while not objects[i] is None :
            if i > self.countItemsPerSong:
                break
                # print objects[i]
            song = Song()

            song.artist = objects[i]["artist"]
            song.name = objects[i]["title"]
            song.url = objects[i]["url"]
            head = r.head(song.url)
            song.size = float( head.headers["content-length"] )
            song.duration = float( objects[i]["duration"] )
            song.bitrate = (song.size * 8 / song.duration) / 1024

            songName = song.artist + song.name

            #Check does song name already exist
            if songName in songsNames:
                self.recursiveGetName(song, songsNames, 0)

            songsNames.append(song.artist + song.name)
            songs.append(song)
            i+=1

        return songs

    def recursiveGetName(self, song, songsNames, number):
        songName = song.artist + song.name + "(" + str(number) + ")"
        if songName in songsNames:
            self.recursiveGetName(song, songsNames, number + 1)
        else:
            song.name = song.name + "(" + str(number) + ")"

    def filterSongs(self, songs = [Song(),]):
        filteredSongs = []
        for song in songs:
            if song.bitrate > self.filterBitrate:
                filteredSongs.append(song)

        return filteredSongs

down = Downloader()
down.download()

    # def sortSongs(self, songs):







# ------------------------------------------------------------------------------------------------------------------

# def jsonGetUrl(Url, PostData = None, Opener=None):
#     req = urllib2.Request(Url, PostData, {'Content-Type': 'application/json'})
#     if Opener:
#         u = Opener.open(req, timeout=HTTP_TIMEOUT)
#     else:
#         u = urllib2.urlopen(req)
#     resp = u.read()
#     u.close()
#     return resp
#
# class Settings:
#     def __init__(self):
#         self.baseUrl = RPC_HOST + RPC_PATH
#
# class UserInfo:
#     def __init__(self):
#         self.username = USER_NAME
#         self.password = USER_PASSWORD
#         self.listenerId = ''
#         self.authToken = ''
#
#
# class PartnerInfo:
#     def __init__(self):
#         self.In = ''
#         self.out = ''
#         self.authToken = ''
#         self.device = DEVICE
#         self.login = PARTNER_LOGIN
#         self.password = PARTNER_PASSWORD
#         self.id = 0
#         self.In = Crypto(IN_KEY)
#         self.out = Crypto(OUT_KEY)
#
# class Pandora:
#     def __init__(self):
#         self.partner = PartnerInfo()
#         self.user = UserInfo()
#         self.settings = Settings()
#         self.opener = urllib2.build_opener()
#
#     def partnerLogin(self):
#         postData = json.dumps({"username": self.partner.login,
#                                 "password": self.partner.password,
#                                 "deviceModel": self.partner.device,
#                                 "version": "5",
#                                 "includeUrls": True})
#
#         URL = 'https://' + self.settings.baseUrl + 'method=auth.partnerLogin'
#         response = jsonGetUrl(URL, postData, self.opener)
#         responseJson = json.loads(response)
#
#         if responseJson['stat'] == "ok":
#             print 'PartnerAuthentificate succes.'
#         else:
#             print 'PartnerAuthentificate fail.'
#             return False
#
#         result = responseJson["result"]
#         cryptedTimestamp = result["syncTime"]
#         decryptedTimestamp = self.partner.In.decrypt(cryptedTimestamp)
#         if decryptedTimestamp and len(decryptedTimestamp) > 4:
#             timestamp = long(decryptedTimestamp[4:-2])
#             self.timeOffset = time.time() - timestamp
#
#         self.partner.authToken = result["partnerAuthToken"]
#         self.partner.id = int(result["partnerId"])
#
#         print self.partner.authToken
#         return True
#
#     def userLogin(self):
#         timestamp = time.time() - self.timeOffset
#         postData = json.dumps({"loginType": "user",
#                                "username": self.user.username,
#                                "password": self.user.password,
#                                "partnerAuthToken": self.partner.authToken,
#                                "syncTime": timestamp})
#         encPostData = self.partner.out.encrypt(postData)
#         urlencAuthToken = urllib.quote_plus(self.partner.authToken)
#         Url = 'https://' + self.settings.baseUrl + "method=auth.userLogin&auth_token=%s&partner_id=%i" % (urlencAuthToken, self.partner.id)
#         response = jsonGetUrl(Url, encPostData, self.opener)
#         responseJson = json.loads(response)
#
#         if responseJson['stat'] == "ok":
#             print 'UserAuthentificate succes.'
#         else:
#             print 'UserAuthentificate fail.'
#             return False
#
#         result = responseJson["result"]
#         self.user.listenerId = int(result["userId"])
#         self.user.authToken = result["userAuthToken"]
#         return True
#
#     def getLikedTracks(self):
#         timestamp = time.time() - self.timeOffset
#         postData = json.dumps({"userAuthToken" : self.user.authToken,
#                                "syncTime" : timestamp})
#         encPostData = self.partner.out.encrypt(postData)
#         method = "user.getBookmarks"
#         url = self.constructUrl(method, secure=False)
#         response = jsonGetUrl(url, encPostData, self.opener)
#         responseJson = json.loads(response)
#         print responseJson
#
#         if responseJson['stat'] == "ok":
#             print 'Get liked tracks.'
#         else:
#             print 'Could not get liked tracks.'
#             return False
#
#         result = responseJson["result"]
#         songs = result["songs"]
#         for song in songs:
#             print song["songName"]
#
#     def constructUrl(self, method, secure=False):
#         urlencAuthToken = urllib.quote_plus(self.user.authToken)
#         if secure:
#             prefix = 'https://'
#         else:
#             prefix = 'http://'
#
#         Url = prefix + self.settings.baseUrl + "method=%s&auth_token=%s&partner_id=%i&user_id=%s" % (method,
#                                                                                            urlencAuthToken,
#                                                                                            self.partner.id,
#                                                                                            self.user.listenerId)
#         return Url


# pand = Pandora()
# pand.partnerLogin()
# pand.userLogin()
# pand.getLikedTracks()
