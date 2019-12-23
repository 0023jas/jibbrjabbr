#For Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import JJItem, JJStory, storyReloadConditional
#This is a new line
#For Image Scraping
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, urlretrieve
import re

#For Getting the Time
from datetime import datetime
import time

#hello

# Create your views here.
def JJView(request):

    #-----------------To be functionized-------------------------#
    now = datetime.now()
    current_time = now.hour
    STR = storyReloadConditional.objects.all()
    STR = STR[0].conditional
    print(STR)
    print(current_time)
    
    if(current_time == 17):
        if(STR == "True"):
            print("No Change Necessary")
        else:
            saveStory()
            storyReloadConditional.objects.all().delete()
            storyReloadConditional(conditional="True").save()
    else:
        if(STR == "False"):
            print("No Change Necessary")
        else:
            storyReloadConditional.objects.all().delete()
            storyReloadConditional(conditional="False").save()
    #-------------------------------------------------------------#

    alljjitems = JJItem.objects.all()
    jjstory = JJStory.objects.all()
    jjstory = jjstory[0]
    return render(request, 'index.html',
    {'all_JJ_Items': alljjitems,
     'JJ_Story' : jjstory})

def addJJItem(request):
    new_JJItem = JJItem(content = request.POST['content'])
    new_JJItem.save()
    return HttpResponseRedirect("/jibbrjabbrmain/")

conditional = False
def saveStoryCheck(conditional):
    conditional = True
    return conditional

def saveStory():
    #Delete and Reset the Story
    JJStory.objects.all().delete()
    jJstoryTitle = getStoryTitle()
    jJstoryImg = getStoryImg()
    jJStoryURL = getStoryURL()
    jjstory = JJStory(storyTitle=jJstoryTitle, storyImg=jJstoryImg, storyURL=jJStoryURL)
    jjstory.save()

    #Delete and Reset the User Comments
    JJItem.objects.all().delete()
    

def loadStory():
    html = urlopen("https://www.bbc.com/news")
    bs = soup(html, 'html.parser')
    links = bs.find_all('a', attrs={'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor'})
    link = links[0]
    finalURL = "https://www.bbc.com" + link['href']
    print(finalURL)
    return finalURL

def getStoryURL():
    finalURL = loadStory()
    return finalURL

def getStoryTitle():
    html = urlopen(loadStory())
    bs = soup(html, 'html.parser')
    titles = bs.find_all('h1', attrs={'class':'story-body__h1'})
    title = titles[0]
    finalTitle = title.contents[0]
    print(finalTitle)
    return finalTitle

def getStoryImg():
    html = urlopen(loadStory())
    bs = soup(html, 'html.parser')
    images = bs.find_all('img')

    image1 = images[1]
    image1 = image1['src']

    image2 = images[2]
    image2 = image2['src']

    if len(image1) > 20:
        print("image 1")
        image = image1
    else:
        print("image 2")
        image = image2

    finalImage = image
    return finalImage
    





