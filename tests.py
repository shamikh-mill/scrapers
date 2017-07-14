'''
File for writing quick tests on web scraping for individual web pages. 
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

# http://www.mapsofindia.com/villages/assam/
def get_villages(url): 
	html = urlopen(url)
	soup = BeautifulSoup(html.read(), 'lxml');

	# specific for webpage format: 
	data = soup.findAll('div',attrs={'class':'vill_liking'})
	for div in data:
		links = div.findAll('a')

	villages = [link.text for link in links]
	print (villages, len(villages))
	return villages 


def get_villages2(url): 
	html = urlopen(url)
	soup = BeautifulSoup(html.read(), 'lxml');

	# specific for webpage format: 
	data = soup.find_all('a', href=True)

	villages = [link.text for link in data]
	print (villages, len(villages))
	return villages 


print (get_villages2('http://vlist.in/sub-district/02144.html'))
