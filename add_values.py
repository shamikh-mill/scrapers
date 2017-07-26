import json
import geojson
import math 
import tempfile 

def addValue(): 
	with open('new.geojson') as json_file:
	    json_data = json.load(json_file)

	
	villages = json_data['features']   

	# for village in villages: 		
	# 	village['properties']['electrif_category'] = int(math.floor(float(village['properties']['perc'])))//10 

	for village in villages: 		
		if village['properties']['perc'] == -1: 
			village['properties']['uH'] = -1 
		else: 
			village['properties']['uH'] = int(village['properties']['HH']) - int(village['properties']['eH'])


	# with tempfile.NamedTemporaryFile(dir='.', delete=False) as temp_file:
	#     geojson.dump(temp_file, json_data)
	# os.replace(temp_file.name, 'new.geojson')

	jsonText = json.dumps(json_data)
	newJSONFile = open('data_with_uh.geojson','w')
	newJSONFile.write(jsonText)
	newJSONFile.close()
	return 


if __name__ == '__main__':
	addValue()
