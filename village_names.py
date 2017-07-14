# import os 

# def remove_nan(directory): 
# 	for file in os.listdir(directory):
# 		filename = os.fsdecode(file)
# 		with open(file, 'r') as f:
# 			first_line = f.readline()

# 			if first_line == "None": 
# 				os.remove(file)


# remove_nan('villages')
import json 
import os 

def remove_nan(directory): 
	for file in os.listdir(directory):
		filepath = directory + '/' + file
		json_data=open(filepath).read()
		if 'None' in json_data: 
		 	print (True)
		 	os.remove(filepath)

from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
	remove_nan('geojsons')

