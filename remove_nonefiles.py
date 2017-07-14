# This code is already implemented in main script.py. 

import json 
import os 

def remove_nan(directory): 
	counter = 0 
	for file in os.listdir(directory):
		filepath = directory + '/' + file
		json_data=open(filepath).read()
		if 'None' in json_data: 
		 	counter += 1 
		 	os.remove(filepath)
	return (counter, 'files removed.')


def move_files(): 
	for file in os.listdir('.'):	
		if file.endswith('.geojson'):
			os.rename("./" + file, "./geojsons/" + file)
			

if __name__ == '__main__':
	move_files()
	remove_nan('geojsons')


