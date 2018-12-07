import vk_api
from bs4 import BeautifulSoup as bs
import requests
import re
import wget
import os

ZAPROS = "Цой клип" #Что ищем
FOLDER = "h:/VK_Video_donloads/" #Куда качать
СNT_VIDEO = "10" #Сколько роликов скачать

vk_session = vk_api.VkApi( 'YOU LOGIN VK', 'YOU PASSWORD' )
vk_session.auth()
vk = vk_session.get_api()

patch_folder = FOLDER+ZAPROS
if not os.path.isdir(patch_folder):
    os.makedirs(patch_folder)

for data in vk.video.search(q=ZAPROS, sort=0, count = СNT_VIDEO, hd=1, filters="short")["items"]:
    name = (re.sub( "^\s+|\n|\r|\s+$", '', data["title"]))
    #print (data["player"]) #ссылка на плеер
    player = (data["player"])
    html = requests.get(player)
    soup = bs(html.text, 'lxml' ).findAll('source')[1:]
    try:
        url = ((soup[0]['src']))
        print ("Качаем файл - %s" % name)
        wget.download(url, FOLDER)
    except:
        print ("ошибка")
print ("Скачено!")
