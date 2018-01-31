

#find all a links DONE
#(ideally only with d or d/a)
#(and ideally only the first html one, but would only repeat so ok)
#put into an array DONE ish they are in a csv
#go to next page DONE
#repeat DONE

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
#array started to append all links I scrape into it to then go to noSelenium
startUrlArray = []

#start csv stuff
f = csv.writer(open("DDAscrapings.csv", "w"))
f.writerow(["link", "time"])
#made an array of all sec pages
secPages = ['https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=0','https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=100','https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=200','https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=300','https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=D&SIC=&State=&Country=&CIK=&owner=include&accno=&count=100&start=400']
#will loop through each one and request the data and put into soup variable
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
	for element in soup.findAll('a'):
		#links = element
		#print(links)
		f.writerow([element, datetime.now()]) #WORKS! I now have all a's in csv
	#add to DDAscrapings.csv so I can see if I'm getting what I need

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

