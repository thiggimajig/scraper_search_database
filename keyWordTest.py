#work in progress
#notes number 2

# Get the first 10 hits for "fraud stuff for austin" in Google US
from google import search
import csv

with open('austinScraperTest.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

print(your_list)

name = your_list[0][1][2]
# [['This is the first line', 'Line1'],
#  ['This is the second line', 'Line2'],
#  ['This is the third line', 'Line3']]

f = csv.writer(open("fraudSearchResults.csv", "a"))
f.writerow(["Search Terms", "Top 10 URL"])

#don't overwrite old data open("learner.csv", "w") to open("learner.csv", "a")
#fraudArray = [fraud, jail, prison, ponzi scheme, steal, money laundering, pyramid scheme, stole, investigation, investigated, indicted, corrupt, bribery]



#fullSearch = loop through array and combine with name 

fullSearch = "fraud" + "AND" + name

for url in search(fullSearch, tld='com', lang='en', stop=10):
	print(url)

	f.writerow([fullSearch, url]) 
    


#f.writerow([fullSearch, url]) 


'''error handling:

from xgoogle.search import GoogleSearch, SearchError
try:
  gs = GoogleSearch("quantum mechanics")
  gs.results_per_page = 100
  results = []
  while True:
    tmp = gs.get_results()
    if not tmp: # no more results were found
      break
    results.extend(tmp)
  # ... do something with all the results ...
except SearchError, e:
  print "Search failed: %s" % e ''' 