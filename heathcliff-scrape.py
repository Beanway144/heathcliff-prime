#Script for mass-downloading Heathcliff comics from gocomics.com
from bs4 import BeautifulSoup
import requests
from os.path  import basename
import datetime

imgList = [] #list of src urls of the comics
#get all comics from 2021 and 2022
for y in range(0, 2):
    for m in range (1, 13):
        for d in range(1, 32):
            year = 2021 + y
            month = m
            day = d
            try:
                if datetime.date(year, m, d ).weekday() == 6: continue #ignore sunday comics

                # preparing url suffix
                smonth = str(month)
                if month < 10: smonth = "0" + smonth
                sday = str(day)
                if day < 10: sday = "0" + sday
                date = str(year) + "/" + smonth + "/" + sday

                try:
                    url = "https://www.gocomics.com/heathcliff/" + date
                    req = requests.get(url)
                    soup = BeautifulSoup(req.text, "html.parser")
                    find_by_class = soup.find_all(class_="comic")
                    imgSrc = find_by_class[0]['data-image']
                    imgList.append(imgSrc)

                    #download image
                    img_data = requests.get(imgSrc).content 
                    dir = "./" + str(year) + "-" + smonth + "/"
                    with open(str(year) + "-" + smonth + "-" + sday + ".png", 'wb') as handler: 
                        handler.write(img_data) 
                except:
                    pass
            except: 
                pass
    
