import json
import geojson
import math 
import tempfile 

def addValue(): 
	with open('electricityKnown.geojson') as json_file:
	    json_data = json.load(json_file)

	
	villages = json_data['features']   

	for village in villages: 		
		village['properties']['electrif_category'] = int(math.floor(float(village['properties']['perc'])))//10 


	# with tempfile.NamedTemporaryFile(dir='.', delete=False) as temp_file:
	#     geojson.dump(temp_file, json_data)
	# os.replace(temp_file.name, 'new.geojson')

	jsonText = json.dumps(json_data)
	newJSONFile = open('new.geojson','w')
	newJSONFile.write(jsonText)
	newJSONFile.close()
	return 


if __name__ == '__main__':
	addValue()
