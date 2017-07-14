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
	counter = 0 
	for file in os.listdir(directory):
		filepath = directory + '/' + file
		json_data=open(filepath).read()
		if 'None' in json_data: 
		 	counter += 1 
		 	os.remove(filepath)
	return (counter, 'files removed.')

if __name__ == '__main__':
	remove_nan('geojsons')

