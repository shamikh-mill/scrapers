'''
1. Search for a village on http://nominatim.openstreetmap.org/
2. Get the OSM_id from json response 
JSON: 
3. Search OSM id into Polygon search to retrieve JSON 
'''
import urllib.request, json
import geojson
import tempfile
import os 
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.mapsofindia.com/villages/assam/") 
soup = BeautifulSoup(html.read(), 'lxml');

data = soup.findAll('div',attrs={'class':'vill_liking'})
for div in data:
	links = div.findAll('a')

villages = [link.text for link in links]
print ((villages), len(villages))


def get_id(search): 
	url = 'http://nominatim.openstreetmap.org/search/' + search + '?format=json'
	try: 
		with urllib.request.urlopen(url) as url:
			data = json.loads(url.read().decode()) 
			json_list = [[obj] for obj in data]
			for each in json_list: 
				# if each[0]['type'] == "town" or each[0]['type'] == "village" and each[0]['display_name'][-5:] == "India":
				if each[0]['display_name'][-5:] == "India":
					try: 
						return ((each[0]['osm_id']), search)
					except: 
						print ('Invalid JSON response')
				else: 
					return ('No Indian villages or town in response.')
	except: 
		print ('Village is not available on OSM.')

def get_polygon(params):
	try:  
		url = 'http://polygons.openstreetmap.fr/get_geojson.py?id=' + params[0] + '&params=0'
		try: 
			urllib.request.urlretrieve(url, params[1] + ".geojson")
		except: 
			print ('No geojson object found on OSM.')
	except: 
		print ('Function get_id failed already.')

	
def main(village): 
	print (get_id(village))
	print (get_polygon(get_id(village))) 


if __name__ == '__main__':
	for village in villages: 
		main(village)

# Test cases. 
# 1. Araria 
# 2. Bhagmohabbat
