# -*- coding: iso8859-9 -*-


import urllib2,urllib,re,HTMLParser,cookielib
import sys,os,base64,time
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

__settings__ = xbmcaddon.Addon(id="plugin.video.wft")
__language__ = __settings__.getLocalizedString
downloadFolder = __settings__.getSetting('downloadFolder')
home = __settings__.getAddonInfo('path')
IMAGES_PATH = xbmc.translatePath(os.path.join(home, 'resources','images'))
sys.path.append(IMAGES_PATH)
SUBS_PATH = xbmc.translatePath(os.path.join(home, 'resources', 'subs'))
sys.path.append(SUBS_PATH)
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)
web='aHR0cDovL3RoZW9wZW5nb2FsLmNvbS9wcy9wYXNzLnhtbA=='

def name_prepare(videoTitle):
        print 'DUZELTME ONCESI:',videoTitle
        videoTitle=videoTitle.replace('İzle',"").replace('Türkçe',"").replace('Turkce',"").replace('Dublaj',"|TR|").replace('Altyazılı'," [ ALTYAZILI ] ").replace('izle',"").replace('Full',"").replace('720p',"").replace('HD',"")
        return videoTitle   
        
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        link=link.replace('\xFD',"i").replace('&#39;&#39;',"\"").replace('&#39;',"\'").replace('\xf6',"o").replace('&amp;',"&").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g")
        link=link.replace('\xc5\x9f',"s").replace('&#038;',"&").replace('&#8217;',"'").replace('\xc3\xbc',"u").replace('\xc3\x87',"C").replace('\xc4\xb1',"ı").replace('&#8211;',"-").replace('\xc3\xa7',"c").replace('\xc3\x96',"O").replace('\xc5\x9e',"S").replace('\xc3\xb6',"o").replace('\xc4\x9f',"g").replace('\xc4\xb0',"I").replace('\xe2\x80\x93',"-")
        response.close()
        return link

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player().play(liz)
        return ok



def addDir(name,url,thumbnail,mode,filepath):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumbnail="+urllib.quote_plus(thumbnail)+"&filepath="+urllib.quote_plus(filepath)
        if thumbnail != "":
                thumbnail = os.path.join(IMAGES_PATH, thumbnail+".jpg")
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addvideo(name,url,thumbnail,mode,filepath):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumbnail="+urllib.quote_plus(thumbnail)+"&filepath="+urllib.quote_plus(filepath)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def hata():
        d = xbmcgui.Dialog()
        d.ok('[COLOR red][B]Access Denied to[/B][/COLOR]')
        __settings__.openSettings()
        return xbmc.executebuiltin('Notification("[COLOR red][B]Check Username and Password[/B][/COLOR]")')

def inside():
                cj = cookielib.CookieJar()
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                urllib2.install_opener(opener)
                login= __settings__.getSetting("login")
                if not login:
                        __settings__.openSettings()
                else:
                        pass
                login= __settings__.getSetting("login")
                password= __settings__.getSetting("password")
                key = 'thomasmc'+login+'-'+password+'p'
                resp = opener.open(base64.b64decode(web))
                data=resp.read()
                if key in data:
                        print "Logged in"
                        return True
                else:
                        return xbmc.executebuiltin('Notification("[COLOR red][B]MEMBERS AREA[/B][/COLOR]')
    
def Download_tool():        
        if downloadFolder is '':
                d = xbmcgui.Dialog()
                d.ok('Download Error','You have not set the download folder.\n Please set the addon settings and try again.','','')
                __settings__.openSettings(sys.argv[ 0 ])
        else:
                if not os.path.exists(downloadFolder):
                        print 'Download Folder Doesnt exist. Trying to create it.'
                        os.makedirs(downloadFolder)

def Download_subtitle(videoTitle,url):
        filepath = xbmc.translatePath(os.path.join(SUBS_PATH, str(videoTitle)+'.srt'))
        def download(url, dest):
##                    dialog = xbmcgui.DialogProgress()
##                    dialog.create('Downloading Movie','From Source', filename)
                    urllib.urlretrieve(url, dest, lambda nb, bs, fs, url = url: _pbhook(nb, bs, fs, url,''))
                    print dest
        def _pbhook(numblocks, blocksize, filesize, url = None,dialog = None):
                    try:
                        
                        percent = min((numblocks * blocksize * 100) / filesize, 100)
##                        dialog.update(percent)
                    except:
                        percent = 100
##                        dialog.update(percent)
##                    if dialog.iscanceled():
##                                    dialog.close()
        download(url, filepath)
        iscanceled = True
        xbmc.executebuiltin('Notification("Subtitle","Downloaded")')
        return filepath

def Download_xml(videoTitle,url):
        videoTitle=videoTitle.replace(" ","_")
        filepath = xbmc.translatePath(os.path.join(SUBS_PATH, str(videoTitle)+'.xml'))
        def download(url, dest):
##                    dialog = xbmcgui.DialogProgress()
##                    dialog.create('Downloading Movie','From Source', filename)
                    urllib.urlretrieve(url, dest, lambda nb, bs, fs, url = url: _pbhook(nb, bs, fs, url,''))
                    print dest
        def _pbhook(numblocks, blocksize, filesize, url = None,dialog = None):
                    try:
                        
                        percent = min((numblocks * blocksize * 100) / filesize, 100)
##                        dialog.update(percent)
                    except:
                        percent = 100
##                        dialog.update(percent)
##                    if dialog.iscanceled():
##                                    dialog.close()
        download(url, filepath)
        iscanceled = True
        xbmc.executebuiltin('Notification("Source","Downloaded")')
        return filepath

def check_time(xml):
        try:
                status=''
                t = os.path.getmtime(xml)
                today = time.time()
                diff=today-t
                print diff
                if diff <= 28800:
                        status="GUNCEL"
                else:
                        status="ESKI"
                return status
        except:
                return ["/unable to control " + xml]

def check_xml_status(name,url):
        name=name.replace(" ","_")
        xml = xbmc.translatePath(os.path.join(SUBS_PATH, str(name)+'.xml'))
        Sonuc=check_empty_xml(xml)
        if Sonuc == 'YOK':
                print 'XML YOK'
                xml=Download_xml(name,url)
                print 'XML OLUSTURULDU'
        else:
                print 'XML BULUNDU'
                pass

        status=check_time(xml)
        print "XML DOSYA DURUMU : " +str(status)
        if status == "ESKI":
                print "xml dosya = ESKI / YENIDEN TARANIYOR."
                xml=Download_xml(name,url)
                print 'XML YENILENDI'
                return xml
        
        elif status == "GUNCEL":
                print "VAROLAN XML OKUNUYOR:",xml
                return xml
        else:
                print 'RECENT SONUC :xml degerlendirilemedi'
        
        return xml

def check_empty_xml(xml):
        if os.path.isfile(xml):
                Sonuc='VAR'
        else:
                Sonuc='YOK'
       
        return Sonuc

