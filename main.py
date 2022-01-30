from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get("https://fitgirl-repacks.site/all-my-repacks-a-z/")
time.sleep(10)
listofgames= list()
browser.find_element(By.ID,"smart_push_smio_not_allow").click()
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
   <ol>
"""
htmlend="""
   </ol>
  </body>
 </html
"""
htmlfile.write(htmlstart)
for i in listofgames:
	listring='<li><a href="' + i[1] + '" target="_blank"> '+i[0]+"</a></li>"
	htmlfile.write(listring)
htmlfile.write(htmlend)