#this is working. yay. 1/30/18

import requests
import csv
from lxml import html
import re
#import urllib.request
from bs4 import BeautifulSoup
#import loopingArray why?


#adding in the loopingArray stuff here
#or just use import
#loopurl from loopingarray.py signifies which url we're up to in the loop through the list/array of all sec urls after they go through noselnium manipulator and afater they've been scraped from each 4-5 pages of the website and added to array
# quote_page = loopURL
quote_page = 'https://www.sec.gov/Archives/edgar/data/1718590/000090266417004005/xslFormDX01/primary_doc.xml'
page = requests.get(quote_page)
soup = BeautifulSoup(page.content, 'html.parser')


print(soup.prettify())

f = csv.writer(open("austinScraperTest.csv", "w"))
f.writerow(["Company","FileType", "FileID","First Name", "Middle Name", "Last Name"])

pageContent=requests.get(quote_page)
	#'https://www.sec.gov/Archives/edgar/data/1603418/000160341817000002/xslFormDX01/primary_doc.xml'
    #'https://www.sec.gov/Archives/edgar/data/1685217/000168521717000001/xslFormDX01/primary_doc.xml'

tree = html.fromstring(pageContent.content)
#print(tree)

for element in soup.findAll('span', attrs={'class': 'FormTitle'})[1:2]:
	formTypeTwo = element.get_text()
#print(formTypeTwo)
#formTypeTwo = str(soup.findAll('span', attrs={'class': 'FormTitle'})[1:2])

companyName = str(tree.xpath('/html/body/table[2]/tbody/tr[4]/td/text()'))
cleancompanyName = re.sub('[^A-Za-z0-9]+', '', companyName)
#formType isn't coming in for some reason
formType = str(tree.xpath('/html/body/table[1]/tbody/tr[2]/td[2]/span[3]/text()'))
cleanformType = re.sub('[^A-Za-z0-9]+', '', formType)
fileID = str(tree.xpath('/html/body/table[2]/tbody/tr[2]/td[1]/a/text()'))
cleanfileID = re.sub('[^A-Za-z0-9]+', '', fileID)
#xpath way of locating instead of css selectors 
#we can either try to make a variable for 4, 6, 8 and so on for xpath 
firstName1 = str(tree.xpath('/html/body/table[4]/tbody/tr[2]/td[2]/text()'))
cleanfirstName1 = re.sub('[^A-Za-z0-9]+', '', firstName1)
middleName1 = str(tree.xpath('/html/body/table[4]/tbody/tr[2]/td[3]/text()'))
cleanmiddleName1 = re.sub('[^A-Za-z0-9]+', '', middleName1)
lastName1 = str(tree.xpath('/html/body/table[4]/tbody/tr[2]/td[1]/text()'))
cleanlastName1 = re.sub('[^A-Za-z0-9]+', '', lastName1)


firstName2 = str(tree.xpath('/html/body/table[6]/tbody/tr[2]/td[2]/text()'))
cleanfirstName2 = re.sub('[^A-Za-z0-9]+', ' ', firstName2)
middleName2 = str(tree.xpath('/html/body/table[6]/tbody/tr[2]/td[3]/text()'))
cleanmiddleName2 = re.sub('[^A-Za-z0-9]+', ' ', middleName2)
lastName2 = str(tree.xpath('/html/body/table[6]/tbody/tr[2]/td[1]/text()'))
cleanlastName2 = re.sub('[^A-Za-z0-9]+', ' ', lastName2)

firstName3 = str(tree.xpath('/html/body/table[8]/tbody/tr[2]/td[2]/text()'))
cleanfirstName3 = re.sub('[^A-Za-z0-9]+', '', firstName3)
middleName3 = str(tree.xpath('/html/body/table[8]/tbody/tr[2]/td[3]/text()'))
cleanmiddleName3 = re.sub('[^A-Za-z0-9]+', '', middleName3)
lastName3 = str(tree.xpath('/html/body/table[8]/tbody/tr[2]/td[1]/text()'))
cleanlastName3 = re.sub('[^A-Za-z0-9]+', '', lastName3)
#print(fileID0)
firstName4 = str(tree.xpath('/html/body/table[10]/tbody/tr[2]/td[2]/text()'))
cleanfirstName4 = re.sub('[^A-Za-z0-9]+', '', firstName4)
middleName4 = str(tree.xpath('/html/body/table[10]/tbody/tr[2]/td[3]/text()'))
cleanmiddleName4 = re.sub('[^A-Za-z0-9]+', '', middleName4)
lastName4 = str(tree.xpath('/html/body/table[10]/tbody/tr[2]/td[1]/text()'))
cleanlastName4 = re.sub('[^A-Za-z0-9]+', '', lastName4)

firstName5 = str(tree.xpath('/html/body/table[12]/tbody/tr[2]/td[2]/text()'))
cleanfirstName5 = re.sub('[^A-Za-z0-9]+', '', firstName5)
middleName5 = str(tree.xpath('/html/body/table[12]/tbody/tr[2]/td[3]/text()'))
cleanmiddleName5 = re.sub('[^A-Za-z0-9]+', '', middleName5)
lastName5 = str(tree.xpath('/html/body/table[12]/tbody/tr[2]/td[1]/text()'))
cleanlastName5 = re.sub('[^A-Za-z0-9]+', '', lastName5)

f.writerow([cleancompanyName,formTypeTwo,cleanfileID,cleanfirstName1,cleanmiddleName1,cleanlastName1])
f.writerow(['','','',cleanfirstName2,cleanmiddleName2,cleanlastName2])
f.writerow(['','','',cleanfirstName3,cleanmiddleName3,cleanlastName3])
f.writerow(['','','',cleanfirstName4,cleanmiddleName4,cleanlastName4])
f.writerow(['','','',cleanfirstName5,cleanmiddleName5,cleanlastName5])