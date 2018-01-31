#this works

#Archives/edgar/data/1637199/000163719917000001/0001637199-17-000001-index.htm
#use this
#https://www.sec.gov/Archives/edgar/data/1637199/000163719917000001/0001637199-17-000001-index.htm
#and this
#https://www.sec.gov/Archives/edgar/data/1637199/000163719917000001/xslFormDX01/primary_doc.xml
#to make this
#https://www.sec.gov
#xslFormDX01/primary_doc.xml

# in python I need to take a base url X
# then I need to add Y to the front
# and then replace end bit with
# a different end bit 


startUrl = '/Archives/edgar/data/1718590/000090266417004005/0000902664-17-004005-index.htm'

frontAdd = 'https://www.sec.gov'

#findReplaceF = '0001637199-17-000001-index.htm'#30 characters from the end?
#this equals sixth "/"
#replace() is a method of <class 'str'> in python3:
#>>> 'hello, world'.replace(',', ':')
#'hello: world'

endAdd = '/xslFormDX01/primary_doc.xml'

#newStartUrl = str(startUrl).replace('0001637199-17-000001-index.htm','xslFormDX01/primary_doc.xml')

#newerStartUrl = startUrl.rsplit('/',-5)
#or this may not work or it may not delete the last bit
#print(newerStartUrl)
#didn't work

betterStarturl = startUrl.rsplit('/', 6) #or 5
#print(orNewerStarturl)
del betterStarturl[-1]
#print(orNewerStarturl)

s = "/"
finalStartUrl = (s.join(betterStarturl))
#print(finalStartUrl)
#newStartUrlTwo = orNewerStarturl.join

endUrl = frontAdd + finalStartUrl + endAdd

print(endUrl)

#Then you use it https://www.sec.gov/Archives/edgar/data/1525542/000150794318000018/0001507943-18-000018-index.htm 
	#to manipulate into https://www.sec.gov/Archives/edgar/data/1525542/000150794318000018/xslFormDX01/primary_doc.xml by saying after 5th backslash delete then add to back

#now I need to create an array of all the archives from 
#all the pages from 0 - 400 then run them all through this script
#and get the final link we need to use the scraper on
#We may need to deal with the google search script in bulk/array not sure
#
#
#
#
#
#print(newStartUrl)
#both newstarturl and endurl worked yay!
#
#
#can easily add the replace part to the end if I can just figure out how 
#to delete the right part
#str.split([sep[, maxsplit]])
#>>> s = 'https://docs.python.org/3.4/tutorial/interpreter.html'
#['https://docs.python.org/3.4/tutorial', 'interpreter.html']
#>>> s.rsplit('/',1)[1]
#'interpreter.html'
