import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddon,xbmcvfs
import os,base64,time

# -*- coding: iso-8859-9 -*-

__settings__ = xbmcaddon.Addon(id='plugin.video.wft')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'Fanart.jpg' ) )
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)
import paytools
l_check=paytools.inside()
if l_check:
        pass
else:
        paytools.hata()
        sys.exit()

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

thomast='aHR0cDovL3RoZW9wZW5nb2FsLmNvbS9hcHAvYmFubmVyLmpwZw=='
payurl='aHR0cDovL3Nwb3J0aW5nc3RyZWFtcy5uZXQ='
heygidi='http://xbmctr.com'

urll='aHR0cDovL2NyaWNmcmVlLnN4L2xpdmUvd2F0Y2gtbGl2ZS1mb290YmFsbC1zdHJlYW0='
livet='special://home/addons/plugin.video.PayPay/resources/images/livet.png'

hangii='aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20v'



sky1='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDE/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
sky2='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDI/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
sky3='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDM/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
sky4='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDQ/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
sky5='cnRtcDovLzMxLjIyMC4wLjgyOjE5MzUvbGl2ZSBwbGF5cGF0aD1zNSBzd2ZVcmw9aHR0cDovL3d3dy5mbGFzaHR2LmNvL2VQbGF5ZXJyLnN3ZiBsaXZlPTEgcGFnZVVybD1odHRwOi8vd3d3LmZsYXNodHYuY28vIHRva2VuPSVaWnJpKG5LYUAjWg=='
skyf1='cnRtcDovLzMxLjIyMC4wLjgyOjE5MzUvbGl2ZSBwbGF5cGF0aD1zZjF4IHN3ZlVybD1odHRwOi8vd3d3LmZsYXNodHYuY28vZVBsYXllcnIuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuZmxhc2h0di5jby8gdG9rZW49JVpacmkobkthQCNa='
skynews='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDU/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
bt1='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDY/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
bt2='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDc/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
box='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDk/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
horse='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDEwP3M9TUJYcmYgYXBwPWxpdmUgbGl2ZT10cnVl='
itvhd='aHR0cDovL3R2Y2F0Y2h1cC1saXZlLmhscy5hZGFwdGl2ZS5sZXZlbDMubmV0L3R2Y2F0Y2h1cC0yMDEvc21pbDppdHZvbmVfZGVza193aWZpLnNtaWwvY2h1bmtsaXN0X2IxNjAwMDAwLm0zdTg='
bbconehd='aHR0cDovL3R2Y2F0Y2h1cC1saXZlLmhscy5hZGFwdGl2ZS5sZXZlbDMubmV0L3R2Y2F0Y2h1cC0yMDEvc21pbDpiYmNvbmVfZGVza193aWZpLnNtaWwvY2h1bmtsaXN0X2IxNjAwMDAwLm0zdTg='
bein1='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxIHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein2='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MyIHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein3='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MzIHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein4='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2M0IHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein5='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2M1IHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein6='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2M2IHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein7='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2M3IHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein8='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2M4IHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein9='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2M5IHN3ZlVybD1odHRwOi8vd3d3LmhkY2FzdC5vcmcvcGxheWVycy5zd2YgbGl2ZT0xIHBhZ2VVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnLyB0b2tlbj0jeXcldHQjd0Bra3U='
bein10='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxMCBzd2ZVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnL3BsYXllcnMuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuaGRjYXN0Lm9yZy8gdG9rZW49I3l3JXR0I3dAa2t1='
bein11='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxMSBzd2ZVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnL3BsYXllcnMuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuaGRjYXN0Lm9yZy8gdG9rZW49I3l3JXR0I3dAa2t1='
bein12='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxMiBzd2ZVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnL3BsYXllcnMuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuaGRjYXN0Lm9yZy8gdG9rZW49I3l3JXR0I3dAa2t1='
bein13='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxMyBzd2ZVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnL3BsYXllcnMuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuaGRjYXN0Lm9yZy8gdG9rZW49I3l3JXR0I3dAa2t1='
bein14='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxNCBzd2ZVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnL3BsYXllcnMuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuaGRjYXN0Lm9yZy8gdG9rZW49I3l3JXR0I3dAa2t1='
bein15='cnRtcGU6Ly80Ni4yNDYuMTI0LjI4OjE5MzUvbGl2ZSBwbGF5cGF0aD1qc2MxNSBzd2ZVcmw9aHR0cDovL3d3dy5oZGNhc3Qub3JnL3BsYXllcnMuc3dmIGxpdmU9MSBwYWdlVXJsPWh0dHA6Ly93d3cuaGRjYXN0Lm9yZy8gdG9rZW49I3l3JXR0I3dAa2t1='
ch8='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDg/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU='
ch11='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDExP3M9TUJYcmYgYXBwPWxpdmUgbGl2ZT10cnVl='
ch12='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDEyP3M9TUJYcmYgYXBwPWxpdmUgbGl2ZT10cnVl=' 
ch13='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDEzP3M9TUJYcmYgYXBwPWxpdmUgbGl2ZT10cnVl='
ch14='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDE0P3M9TUJYcmYgYXBwPWxpdmUgbGl2ZT10cnVl='
ch15='cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDE1P3M9TUJYcmYgYXBwPWxpdmUgbGl2ZT10cnVl='
sk1='aHR0cDovLzgzLjEzOS4xMDQuMTAxL0NvbnRlbnQvSExTL0xpdmUvQ2hhbm5lbChTa18xKS9pbmRleC5tM3U4='
sk2='aHR0cDovLzgzLjEzOS4xMDQuMTAxL0NvbnRlbnQvSExTL0xpdmUvQ2hhbm5lbChTa18zKS9pbmRleC5tM3U4='
rena1='aHR0cDovLzg3LjEyMS4zMC4yNTQ6ODAwMS8xOjA6MTk6MWNmOmI6MToxODZhYjdmOjA6MDowOg=='
rena2='aHR0cDovLzg3LjEyMS4zMC4yNTQ6ODAwMS8xOjA6MTk6MWQwOmI6MToxODZhYjdmOjA6MDowOg=='
rena3='aHR0cDovLzg3LjEyMS4zMC4yNTQ6ODAwMS8xOjA6MTk6MWQxOmI6MToxODZhYjdmOjA6MDowOg=='
rena4='aHR0cDovLzg3LjEyMS4zMC4yNTQ6ODAwMS8xOjA6MTk6MWQyOmI6MToxODZhYjdmOjA6MDowOg=='
rena5='aHR0cDovLzgzLjE3Ny4xODEuNTk6ODAwMS8xOjA6MTY6NUY6MTo0MDpBMDAwMDA6MDowOjA6='


def CATEGORIES():
        web='aHR0cDovL3NpbmVtYS54Ym1jdHIudHYv'
        link=get_url(base64.b64decode(web))
        match=re.compile('<li><a href="#" class="toplam">(.*?)</a></li>').findall(link)
        for bul in match:
                bul=''
                print bul
        paypay='aHR0cDovL3Nwb3J0aW5nc3RyZWFtcy5uZXQvd2F0Y2gvbGl2ZWhkcw=='
        hangi='aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vbGl2ZS1mb290YmFsbC1vbi10di8='

        addDir('[COLOR blue][B]>> [COLOR white]TV Schedule[/B][/COLOR]',(base64.b64decode(hangi)),5,'special://home/addons/plugin.video.wft/resources/images/tvguide.png')
        #addDir('[COLOR blue][B]>> [COLOR honeydew]TV Channel List TestLine[/B][/COLOR]',(base64.b64decode(paypay)),1,'special://home/addons/plugin.video.wft/resources/images/banner.jpg')
        addDir('[COLOR blue][B]>> [COLOR white]TV Channel List[/B][/COLOR]',heygidi,4,'special://home/addons/plugin.video.wft/resources/images/banner.jpg')

def listem():
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports 1 HD [/B][/COLOR]',(base64.b64decode(sky1)),3,'special://home/addons/plugin.video.wft/resources/images/ss1.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports 2 HD[/B][/COLOR]',(base64.b64decode(sky2)),3,'special://home/addons/plugin.video.wft/resources/images/ss2.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports 3 HD[/B][/COLOR]',(base64.b64decode(sky3)),3,'special://home/addons/plugin.video.wft/resources/images/ss3.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports 4 HD[/B][/COLOR]',(base64.b64decode(sky4)),3,'special://home/addons/plugin.video.wft/resources/images/ss4.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports 5 SD[/B][/COLOR]',(base64.b64decode(sky5)),3,'special://home/addons/plugin.video.wft/resources/images/ss5.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports News HD[/B][/COLOR]',(base64.b64decode(skynews)),3,'special://home/addons/plugin.video.wft/resources/images/ssn.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Sky Sports F1 SD[/B][/COLOR]',(base64.b64decode(skyf1)),3,'special://home/addons/plugin.video.wft/resources/images/sf1.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] BT Sports 1 HD[/B][/COLOR]',(base64.b64decode(bt1)),3,'special://home/addons/plugin.video.wft/resources/images/bt1.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] BT Sports 2 HD[/B][/COLOR]',(base64.b64decode(bt2)),3,'special://home/addons/plugin.video.wft/resources/images/bt2.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Box Nation HD[/B][/COLOR]',(base64.b64decode(box)),3,'special://home/addons/plugin.video.wft/resources/images/boxt.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Racing UK HD[/B][/COLOR]',(base64.b64decode(horse)),3,'special://home/addons/plugin.video.wft/resources/images/ruk.JPG')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BBC ONE UK HD[/B][/COLOR]',(base64.b64decode(bbconehd)),3,'special://home/addons/plugin.video.wft/resources/images/bbc1.png') 
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] ITV HD[/B][/COLOR]',(base64.b64decode(itvhd)),3,'special://home/addons/plugin.video.wft/resources/images/itvhd.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 1 SD[/B][/COLOR]',(base64.b64decode(bein1)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 2 SD[/B][/COLOR]',(base64.b64decode(bein2)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 3 SD[/B][/COLOR]',(base64.b64decode(bein3)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 4 SD[/B][/COLOR]',(base64.b64decode(bein4)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 5 SD[/B][/COLOR]',(base64.b64decode(bein5)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 6 SD[/B][/COLOR]',(base64.b64decode(bein6)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 7 SD[/B][/COLOR]',(base64.b64decode(bein7)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 8 SD[/B][/COLOR]',(base64.b64decode(bein8)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 9 SD[/B][/COLOR]',(base64.b64decode(bein9)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 10 SD[/B][/COLOR]',(base64.b64decode(bein10)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 11 SD[/B][/COLOR]',(base64.b64decode(bein11)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 12 SD[/B][/COLOR]',(base64.b64decode(bein12)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 13 SD[/B][/COLOR]',(base64.b64decode(bein13)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 14 SD[/B][/COLOR]',(base64.b64decode(bein14)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR lightgreen][B] BEIN 15 SD[/B][/COLOR]',(base64.b64decode(bein15)),3,'special://home/addons/plugin.video.wft/resources/images/bein.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Channel 8[/B][/COLOR]',(base64.b64decode(ch8)),3,'special://home/addons/plugin.video.wft/resources/images/channel.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Channel 11[/B][/COLOR]',(base64.b64decode(ch11)),3,'special://home/addons/plugin.video.wft/resources/images/channel.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Channel 12[/B][/COLOR]',(base64.b64decode(ch12)),3,'special://home/addons/plugin.video.wft/resources/images/channel.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Channel 13[/B][/COLOR]',(base64.b64decode(ch13)),3,'special://home/addons/plugin.video.wft/resources/images/channel.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Channel 14[/B][/COLOR]',(base64.b64decode(ch14)),3,'special://home/addons/plugin.video.wft/resources/images/channel.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Channel 15[/B][/COLOR]',(base64.b64decode(ch15)),3,'special://home/addons/plugin.video.wft/resources/images/channel.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Arena Sport 1[/B][/COLOR]',(base64.b64decode(rena1)),3,'special://home/addons/plugin.video.wft/resources/images/arena1.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Arena Sport 2[/B][/COLOR]',(base64.b64decode(rena2)),3,'special://home/addons/plugin.video.wft/resources/images/arena2.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Arena Sport 3[/B][/COLOR]',(base64.b64decode(rena3)),3,'special://home/addons/plugin.video.wft/resources/images/arena3.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Arena Sport 4[/B][/COLOR]',(base64.b64decode(rena4)),3,'special://home/addons/plugin.video.wft/resources/images/arena4.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] Arena Sport 5[/B][/COLOR]',(base64.b64decode(rena5)),3,'special://home/addons/plugin.video.wft/resources/images/arena5.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] SK1 [/B][/COLOR]',(base64.b64decode(sk1)),3,'special://home/addons/plugin.video.wft/resources/images/sk.png')
        addDir('[COLOR blue][B]>>[/B][/COLOR] [COLOR white][B] SK2 [/B][/COLOR]',(base64.b64decode(sk2)),3,'special://home/addons/plugin.video.wft/resources/images/sk.png')
        
        addDir('[COLOR tomato][B]Live Matches *****[/B][/COLOR]', "ayniyim(url)",'','special://home/addons/plugin.video.wft/icon.png')
        link=get_url(base64.b64decode(urll))
        match2=re.compile('<td style="color:#7BA314;font-weight:bold; font-size: small" width=".*?" class="matchtime">(.*?)</td>\n\t\t\t\t\t\t\t<td style=".*?" width=".*?">(.*?)</td>\n\n\t\t\t\t\t\t\t\t<td width=".*?"> \t<img src=".*?" /></td>\n\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</table>\n\n\t\t\t\t\t\t<div style=".*?" class="hidden"><a target=\'_blank\' href=\'(.*?)\' ').findall(link)
        for saat,name,url in match2:
            name=name+' '+'[COLOR beige]'+saat+'[COLOR yellow]'+'GMT[/COLOR]'
            addDir('[COLOR blue][B]>> [/B][/COLOR][COLOR orange][B]'+name+'[/B][/COLOR]',url,7,livet)
            
def paypay(url):
        link=get_url(url)
        match=re.compile(' id=".*?" class="ch-link" href="(.*?)">.*? - (.*?)</a>').findall(link)
        for url,name in match:              
                url=(base64.b64decode(payurl))+url
                addDir('[COLOR lightgreen][B]>> [COLOR lightblue][B]'+name+'[/B][/COLOR]',url,2,(base64.b64decode(thomast)))

def paypayyayin(name,url):
        link=get_url(url)
        match=re.compile(' value="src=rtmp:\/\/.*?\/live\/channel(.*?)\%3(.*?)%3(.*?)\&controlBarAutoHideTimeout').findall(link)
        for bir,iki,uc in match:
                xbmcPlayer = xbmc.Player()
                playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playList.clear()
                bir=bir+'?'
                iki=iki+'='
                #rtmp://vdn.sportingstreams.net:443/live playpath=channel1?s=MBXrf app=live live=true
                url='rtmp://vdn.sportingstreams.net:443/live playpath=channel'+bir+iki+uc+' app=live live=true'

                #rtmp://vdn.sportingstreams.net:443/live playpath=channel=cnRtcDovL3Zkbi5oZC1zdHJlYW1pbmcudHY6NDQzL2xpdmUgcGxheXBhdGg9Y2hhbm5lbDE/cz1NQlhyZiBhcHA9bGl2ZSBsaXZlPXRydWU= app=live live=true
                
                url=url.replace('Fs','s').replace('DMBXrf','MBXrf')
                addLink(name,url,livet)
        if playList:
                xbmcPlayer.play(playList)

def yayin(name,url):
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()

        addLink(name,url,livet)
        listitem = xbmcgui.ListItem(name)
        playList.add(url, listitem)
        xbmcPlayer.play(playList)
        
        i = dialog.ok('Have Fun !!!', "[COLOR beige]Have Fun[/COLOR]","[COLOR pink] Have Fun.[/COLOR]")

def hangi(url):
        link=get_url(url)
        addDir('[COLOR blue][B]***** [COLOR lightblue]Todays Schedule[COLOR blue][B] *****[/B][/COLOR]', '',4,'special://home/addons/plugin.video.wft/icon.png')
        addDir('[COLOR blue][B] [/B][/COLOR]', "ayniyim(url)",'','special://home/addons/plugin.video.wft/icon.png')
        match=re.compile('<span class="fixture"><a href="../(.*?)">\r\n                    (.*?)\r\n                    vs\r\n                    (.*?)</a></span> <span class="ground">\r\n                      \r\n                         (.*?)\r\n').findall(link)
        for url,bir,iki,saat in match:
            name='[COLOR beige]'+bir+'[COLOR lightblue] vs '+'[COLOR beige]'+iki+' '+'[COLOR yellow]'+saat
            url=base64.b64decode(hangii)+url
            addDir('[COLOR blue][B] >> [/B][/COLOR][COLOR orange][B]'+name+'[/B][/COLOR]',url,6,'')
        addDir('[COLOR blue][B] [/B][/COLOR]', "ayniyim(url)",'','special://home/addons/plugin.video.wft/icon.png')
        addDir('[COLOR tomato][B]***** Live Matches *****[/B][/COLOR]', "ayniyim(url)",'','special://home/addons/plugin.video.wft/icon.png')
        addDir('[COLOR blue][B] [/B][/COLOR]', "ayniyim(url)",'','special://home/addons/plugin.video.wft/icon.png')
        link=get_url(base64.b64decode(urll))
        match2=re.compile('<td style="color:#7BA314;font-weight:bold; font-size: small" width=".*?" class="matchtime">(.*?)</td>\n\t\t\t\t\t\t\t<td style=".*?" width=".*?">(.*?)</td>\n\n\t\t\t\t\t\t\t\t<td width=".*?"> \t<img src=".*?" /></td>\n\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</table>\n\n\t\t\t\t\t\t<div style=".*?" class="hidden"><a target=\'_blank\' href=\'(.*?)\' ').findall(link)
        for saat,name,url in match2:
            name=name+' '+'[COLOR beige]'+saat+'[COLOR yellow]'+'GMT[/COLOR]'
            addDir('[COLOR blue][B]>> [/B][/COLOR][COLOR orange][B]'+name+'[/B][/COLOR]',url,7,livet)

def hangikanal(url):
        link=get_url(url)
        match2=re.compile('<h2><a href=".*?"><img title=".*?" src=".*?" alt="" /></a>&nbsp;(.*?)&nbsp;<a href=".*?"><img title=".*?" src=".*?" alt="" /></a></h2>\r\n   \t<span class="live">Live on (.*?)</span>\r\n').findall(link)
        for bir,iki in match2:
                name=bir+'[COLOR lightblue] Live ON [COLOR lightgreen]'+iki+'[/COLOR]'

        match=re.compile('<div class="channel-logo"> <a href=""><img src="../(.*?)" alt=".*?"').findall(link)
        for t in match:
                t=(base64.b64decode(hangii))+t.encode('utf-8', 'ignore')
                addDir('[COLOR blue][B] >> [/B][/COLOR][COLOR orange][B]'+name+'[/B][/COLOR]',url,4,t)
        match1=re.compile('<div class="channel-logo"> <a href=".*?"><img src="../(.*?)" alt=".*?"').findall(link)
        for t in match1:
                t=(base64.b64decode(hangii))+t.encode('utf-8', 'ignore')
                addDir('[COLOR blue][B] >> [/B][/COLOR][COLOR orange][B]'+name+'[/B][/COLOR]',url,4,t)

def icerik(name,url):
        link=get_url(url)
        match=re.compile('<iframe frameborder="0" marginheight="0" marginwidth="0" height="490" src="(.*?)"').findall(link)
        for url2 in match:
                link=get_url(url2)
                match=re.compile('fid=\'(.*?)\';').findall(link)
                for kanal in match:
                        #rtmp://31.220.0.195:1935/live playpath=channel4 swfUrl=http://www.flashtv.co/ePlayerr.swf token=%ZZri(nKa@#Z pageUrl=http://www.flashtv.co/embed.php?live=channel4&vw=620&vh=490 live=1
                        url='rtmp://31.220.0.195:1935/live playpath='+kanal+' swfUrl=http://www.flashtv.co/ePlayerr.swf token=%ZZri(nKa@#Z pageUrl=http://www.flashtv.co/embed.php?live='+kanal+'&vw=620&vh=490 live=1'
                        playList.clear()
                        addLink(name,url,livet)
                        listitem = xbmcgui.ListItem(name)
                        playList.add(url, listitem)
                        xbmcPlayer.play(playList)

################################################# 

def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        CATEGORIES()

elif mode==1:
        paypay(url)

elif mode==2:
        paypayyayin(name,url)

elif mode==3:
        yayin(name,url)

elif mode==4:
        listem()

elif mode==5:
        hangi(url)

elif mode==6:
        hangikanal(url)

elif mode==7:
        icerik(name,url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
