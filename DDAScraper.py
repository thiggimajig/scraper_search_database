#step 1 

#find all a links DONE
#(ideally only with d or d/a)
#(and ideally only the first html one, but would only repeat so ok)
#put into an array DONE ish they are in a csv
#go to next page DONE
#repeat DONE
#
#2/1/18 update:
#scrape the file links and put into csv
#take that link 
#(after I need to clean it) cleaned in noSelenium.py
#and adjust so correct final link
#scrape that final link and print necessary info to csv 
#(need to create a loop on all links) 

#use pandas to analyze form type D or D/A against link? if desperate..

#how do I find and grab all links after D and D/A text only
#or first link after D and D/A text 
#
#using https://www.dataquest.io/blog/web-scraping-tutorial-python/
from datetime import datetime
import requests
from lxml import html
import re
import csv
from bs4 import BeautifulSoup
import pandas as pd


#array started to append all links I scrape into it to then go to noSelenium
startUrlArray = []

#start csv stuff
f = csv.writer(open("DDAscrapings.csv", "w"))
f.writerow(["link", "time"])
#made an array of all sec pages
secPages = ['https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=0']#,'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=100']#,'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=200','https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=300','https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=400']
#will loop through each one and request the data and put into soup variable

#to be polite and not slam the sec server
import time
for pg in secPages:
    page = requests.get(pg)
       
    time.sleep(5)  # wait 5 seconds before we make the next request


for pg in secPages:
#first page, maybe loop through 1 to 5 after defining them all 
#sec_page_1 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=0'
#sec_page_2 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=100'
#sec_page_3 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=200'
#sec_page_4 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=300'
#sec_page_5 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=400'

	page = requests.get(pg)
	
	soup = BeautifulSoup(page.content, 'html.parser')
	soup.prettify()
	#print(soup.prettify())
	#
	#trying to only scrape D/A and D
	#soup.find("div", id="search-results").find_all("a", "external-links"):
	#for element in soup.find('td', {'nowrap': "nowrap"}).find_all('a'):

		
	for element in soup.findAll('a'):

    	#links = element
		print(element)	
		f.writerow([element, datetime.now()]) #WORKS! I now have all a's in csv
	#add to DDAscrapings.csv so I can see if I'm getting what I need

#try with pandas
#pandas needs to receive a list or put index in for scalar values 
#https://stackoverflow.com/questions/17839973/construct-pandas-dataframe-from-values-in-variables


#TO DO
#do this next http://newcoder.io/scrape/part-3/ to set up postgres on personal computer
#Schedule for each day (using cron job https://en.wikipedia.org/wiki/Cron#Predefined_scheduling_definitions ) 
	
		longlinks = pd.DataFrame({
				"links": [element],
			#"datetime": [datetime.now()]
 			})
		print(longlinks)

#df = pd.read_csv('DDAscrapings.csv', sep=',')
#print(df)


#perhaps helpful for specifiying D and D/A
#from https://stackoverflow.com/questions/45653935/web-scraping-both-html-text-and-image-link-with-python-beautifulsoup?rq=1
# player_data = []
# for tr in data_rows:
#     tdata = []
#     for td in tr:
#         tdata.append(td.getText())

#         if td.div and td.div['class'][0] == 'school-logo':
#             tdata.append(td.div.a['href'])

#     player_data.append(tdata)




		#tried and failed here to denest the a links i get returned in links so i can strip and add to a clean list to be looped through. 
		#maybe I just need to try cleaning/trimming first
		# for i in links:
		# 	if isinstance(i, list):
		# 		startUrlArray.extend(i)
		# 	else:
		# 		startUrlArray.append(i)
		# print(startUrlArray)

# for element in soup.findAll('td', attrs={'nowrap': 'nowrap'}):
# 	tag = element
# 	dForm = tag.find_all('a')
# 	print(dForm) #this just got me WAY closer. now I can use first soup to somehow only find D or DA THEN get link


#startUrlArray.extend(dForm) #using extend merely took the last element out of a nested list and put it in one list. using append tacked on the last item as a nested list.
#print(startUrlArray)
#now add to an array

#ugh I want this to work here.... 
#for element in soup.findAll(text=re.compile('D/A')):
#	tag2 = element
#	D2 = tag2.find_all('a')
#	print(D2)
	#print(element)
	#DDA = element.get_text() 
	#print(DDA) #so this successfully prints all in nowrap

#I think I want something like this 
#D = soup.find_all('a') #text='D'
#print(D)
#use pandas to analyze form type D or D/A against link? if desperate..

