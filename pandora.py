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

PATT = re.compile(">(.*?)<")

#https://oauth.vk.com/authorize?client_id=3608669&scope=audio&redirect_uri=https://oauth.vk.com/blank&display=wap&response_type=token

COOKIE = 'at=ws6AubkvPAJPa7/yBBp4r7eAaoBzxe5LzOYFma5p7FzY9h+RXT2SvmhU8WZ6DY6R6pBRF9pvcMFm+aO3CSzeYvw%3D%3D'
ACCESS_TOKEN = "8785c8a25541565bcb76555f76eaa8159442e54ec4c2aab64610626d635104e39acc82143853a8445816e"
COUNT_OF_SONGS = 100
COUNT_OF_DUPLICATES = 3
DOWNLOAD_FOLDER_NAME = "audio"
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

def get_names(n = COUNT_OF_SONGS):
    l = 1000
    i = 1
    out = []
    count = 1
    while l>100:
        if not n is None:
            if i >= n:
                break
        resp = r.get("http://www.pandora.com/content/tracklikes?likeStartIndex=0&thumbStartIndex="+str(count)+"&webname="+LOGIN,
             headers = {"Cookie": COOKIE})
        soup = bs.BeautifulSoup(resp.text)
        #print soup
        for x in soup.findAll(attrs={"class":"infobox-body"}):
            patt = [PATT.findall(str(x.a))[0], PATT.findall(str(x.p.a))[0]]
            if patt not in out:
                out.append([PATT.findall(str(x.a))[0], PATT.findall(str(x.p.a))[0]])
            i += 1
            
        if not "infobox-body" in resp.text and not "no_more tracklike" in resp.text:
            print "Something bad. Check your cookie"
            exit()
            
        l = len(resp.text)
        count += 1
        
    print len(out)
    print out
    return out


def audio_search(string):
    resp = r.get("https://api.vk.com/method/audio.search?q=%(q)s&sort=2&count=30&access_token=%(ACCESS_TOKEN)s"%{"q":string, "ACCESS_TOKEN":ACCESS_TOKEN})
    return resp.json()

def fillObjectsInfo(objects):
    i = 1
    fillingObjects = {}

    while not objects[i] is None :
        if i > 10:
            break
            # print objects[i]
        head = r.head(objects[i]["url"])
        size = head.headers["content-length"]
        duration = objects[i]["duration"]
        bytrate = (float(size) * 8 / float(duration)) / 1024
        if bytrate > 300:
            fillingObjects[bytrate] = objects[i]
        i+=1

    return fillingObjects

def sortObjects(objects):
    sortedObjects = []
    count = 0
    copies = COUNT_OF_DUPLICATES
    for key in sorted(objects.keys(), reverse=True):
        if count >= copies:
            break
        sortedObjects.append(objects[key])
        count+=1

    return sortedObjects

def download(folder=DOWNLOAD_FOLDER_NAME):
    if not os.path.exists(folder):
        os.mkdir(folder)
    for song in get_names():
        if len(song) == 1:
            song.append("Unknown")
        try:
            originalSongName = song[0]+" "+song[1]
            objects = audio_search(originalSongName)["response"]
            unsortedObject = fillObjectsInfo(objects)

        except:
            continue

        sortedObjects = sortObjects(unsortedObject)


        for obj in sortedObjects:
            print "start to download", obj["title"] + "-"+obj["artist"]
            try:
                songPath = os.path.join(folder, originalSongName)
                if not os.path.exists(songPath):
                    os.mkdir(songPath)

                urllib.urlretrieve(obj["url"], os.path.join(songPath,  obj["title"] + "-"+obj["artist"] +".mp3"))
            except:
                print 'Download fault'
                continue
            print obj["title"] + "-"+obj["artist"], "downloaded"


            

# download()


# ------------------------------------------------------------------------------------------------------------------

def jsonGetUrl(Url, PostData = None, Opener=None):
    req = urllib2.Request(Url, PostData, {'Content-Type': 'application/json'})
    if Opener:
        u = Opener.open(req, timeout=HTTP_TIMEOUT)
    else:
        u = urllib2.urlopen(req)
    resp = u.read()
    u.close()
    return resp

class Settings:
    def __init__(self):
        self.baseUrl = RPC_HOST + RPC_PATH

class UserInfo:
    def __init__(self):
        self.username = USER_NAME
        self.password = USER_PASSWORD
        self.listenerId = ''
        self.authToken = ''


class PartnerInfo:
    def __init__(self):
        self.In = ''
        self.out = ''
        self.authToken = ''
        self.device = DEVICE
        self.login = PARTNER_LOGIN
        self.password = PARTNER_PASSWORD
        self.id = 0
        self.In = Crypto(IN_KEY)
        self.out = Crypto(OUT_KEY)

class Pandora:
    def __init__(self):
        self.partner = PartnerInfo()
        self.user = UserInfo()
        self.settings = Settings()
        self.opener = urllib2.build_opener()

    def partnerLogin(self):
        postData = json.dumps({"username": self.partner.login,
                                "password": self.partner.password,
                                "deviceModel": self.partner.device,
                                "version": "5",
                                "includeUrls": True})

        URL = 'https://' + self.settings.baseUrl + 'method=auth.partnerLogin'
        response = jsonGetUrl(URL, postData, self.opener)
        responseJson = json.loads(response)

        if responseJson['stat'] == "ok":
            print 'PartnerAuthentificate succes.'
        else:
            print 'PartnerAuthentificate fail.'
            return False

        result = responseJson["result"]
        cryptedTimestamp = result["syncTime"]
        decryptedTimestamp = self.partner.In.decrypt(cryptedTimestamp)
        if decryptedTimestamp and len(decryptedTimestamp) > 4:
            timestamp = long(decryptedTimestamp[4:-2])
            self.timeOffset = time.time() - timestamp

        self.partner.authToken = result["partnerAuthToken"]
        self.partner.id = int(result["partnerId"])

        print self.partner.authToken
        return True

    def userLogin(self):
        timestamp = time.time() - self.timeOffset
        postData = json.dumps({"loginType": "user",
                               "username": self.user.username,
                               "password": self.user.password,
                               "partnerAuthToken": self.partner.authToken,
                               "syncTime": timestamp})
        encPostData = self.partner.out.encrypt(postData)
        urlencAuthToken = urllib.quote_plus(self.partner.authToken)
        Url = 'https://' + self.settings.baseUrl + "method=auth.userLogin&auth_token=%s&partner_id=%i" % (urlencAuthToken, self.partner.id)
        response = jsonGetUrl(Url, encPostData, self.opener)
        responseJson = json.loads(response)

        if responseJson['stat'] == "ok":
            print 'UserAuthentificate succes.'
        else:
            print 'UserAuthentificate fail.'
            return False

        result = responseJson["result"]
        self.user.listenerId = int(result["userId"])
        self.user.authToken = result["userAuthToken"]
        return True

    def getLikedTracks(self):
        timestamp = time.time() - self.timeOffset
        postData = json.dumps({"userAuthToken" : self.user.authToken,
                               "syncTime" : timestamp})
        encPostData = self.partner.out.encrypt(postData)
        method = "user.getBookmarks"
        url = self.constructUrl(method, secure=False)
        response = jsonGetUrl(url, encPostData, self.opener)
        responseJson = json.loads(response)
        print responseJson

        if responseJson['stat'] == "ok":
            print 'Get liked tracks.'
        else:
            print 'Could not get liked tracks.'
            return False

        result = responseJson["result"]
        songs = result["songs"]
        for song in songs:
            print song["songName"]

    def constructUrl(self, method, secure=False):
        urlencAuthToken = urllib.quote_plus(self.user.authToken)
        if secure:
            prefix = 'https://'
        else:
            prefix = 'http://'

        Url = prefix + self.settings.baseUrl + "method=%s&auth_token=%s&partner_id=%i&user_id=%s" % (method,
                                                                                           urlencAuthToken,
                                                                                           self.partner.id,
                                                                                           self.user.listenerId)
        return Url


pand = Pandora()
pand.partnerLogin()
pand.userLogin()
pand.getLikedTracks()
