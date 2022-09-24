from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
browser = webdriver.Firefox()
browser.get("https://fitgirl-repacks.site/all-my-repacks-a-z/")
time.sleep(10)
listofgames= list()
#browser.find_element(By.ID,"smart_push_smio_not_allow").click()
tpage=browser.find_element(By.CLASS_NAME,"lcp_paginator")
tlipage=tpage.find_elements(By.TAG_NAME,"li")
finalpage=int(tlipage[-2].text)
for pageno in range(1,finalpage+1):
	Li =browser.find_element(By.CLASS_NAME,"lcp_catlist")
	lilist = Li.find_elements(By.TAG_NAME,"li")
	for i in lilist:
		if "Multiplayer" in i.text:
			gamename=i.text
			gamelink=i.find_element(By.TAG_NAME,"a").get_attribute("href")
			gametuple=(gamename,gamelink)
			listofgames.append(gametuple)
	if pageno!= finalpage:
		nextpagelink=browser.find_element(By.LINK_TEXT,"Next Page")
		nextpagelink.click()
browser.quit()
htmlfile=open(r"ListofGames.html","w")
htmlstart="""
<html>
 <body>
  <h1>List of Multiplayer Games </h1>
   <table>
"""
htmlend="""
   </table>
  </body>
 </html
"""
htmlfile.write(htmlstart)
datetimelist = []
newlistofgames = []
for i in listofgames:
    r = requests.get(i[1])
    soup = BeautifulSoup(r.text,'html.parser')
    datetime = soup.find_all('time',class_ = 'entry-date')[0]['datetime']
    print(datetime)
    datetimelist.append(datetime)
    newlistofgames.append((datetime,i[0], i[1],soup.find_all('time',class_ = 'entry-date')[0].get_text()))
newlistofgames.sort()
count = 0
for i in newlistofgames:
    count=count+1
    listring='<td><a href="'+i[2]+'" target="_blank"> '+i[1]+"</a></td><td>"+i[3]+"</td></tr>"
    listring='<tr><td>' + str(count) + '</td>' + listring
    htmlfile.write(listring)
htmlfile.write(htmlend)