"""
Utils function libary for Data Extraction Pipeline. Should be in the same directory as feature_extraction.ipynb.

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv
import math
from skimage import io
import re


def confirm_utils():
    return ('Utilities library successfully loaded.') 

def create_csv(feature_labels, VIIRS_IMAGE_PATH = "./indian_village_dataset/imagery_res30_48bands/", 
    MASK_IMAGE_PATH = "./indian_village_dataset/masks_res30/", csv_name = 'output.csv', debug = False): 

    files = [file for file in os.listdir(MASK_IMAGE_PATH) if file.endswith('.tif')] 

    if (debug): 
        files = np.random.choice(files, 100) 
        print ("Debug = True: Testing on 100 villages.") 
    else: 
        print ("Debug = False: Running for all {} villages.".format(len(files)))

    features, village_ids = np.array([]), np.array([])
    counter_invalid, id_invalid, error_image = 0, 0, 0

    print('Initialized file reading.')
    for i, file in enumerate(files):
        
        try: 
            im = io.imread(VIIRS_IMAGE_PATH + file) # read image
            regexp = re.search('([0-9])\w+', file) # check for numbers in filename 
            # check for invalids  
            if im.shape[2] < 47: 
                counter_invalid += 1
            elif type(regexp) == type(None): 
                id_invalid += 1
            else:
                lights = im[:, :, 47]  # get lights at night band
                mask = io.imread(MASK_IMAGE_PATH + file)
                valid_lights = lights[mask>0]

                stats = np.percentile(valid_lights, [0,10,50,90,100], interpolation='nearest') # min, 10p, med, 90p, max 
                mean = np.mean(valid_lights) 
                variance_lights = np.std(valid_lights) # standard dev 
                sum_lights = np.sum(valid_lights) # total_lan (sum)
                area = len(lights) # area 
                stats = np.append(stats, [mean, variance_lights, sum_lights, area])

                village_id = str(file).split('-')[-1][:-4]
                village_ids = np.append(village_ids, village_id)
                for x in range(0, 47): # for everything except lan, add all features to a list, then add list to features. 
                    layer = im[:, :, x]
                    if len(layer) == 0:
                        counter_invalid += 1 
                    else: 
                        valid_layer = layer[mask>0]
                        more_features = [np.amax(valid_layer), np.mean(valid_layer), np.std(valid_layer), np.median(valid_layer),
                                   np.sum(valid_layer), np.percentile(valid_layer, 10, interpolation='nearest'),
                                   np.percentile(valid_layer, 90, interpolation='nearest')] # add here 
                        stats = np.append(stats, more_features, axis=0)
             #   assertEqual(len(stats), len(feature_labels), msg='Number of feature labels != Number of features extracted!')
                if len(feature_labels) == len(stats): 
                    features = np.append(features, stats, axis=0)
            #features.append(stats)
            # print (len(feature_labels), len(stats))
            # print (features.shape)
            if i % (len(files)//10) == 0: # print message every ~10,000 files, just to know it's working
                print ('{} of {} image files read.'.format(i, len(files)))
        except: 
            counter_invalid += 1
    
    print ('Number of invalid images: {}, number of invalid IDs: {}'.format(counter_invalid, id_invalid))
    features = features.reshape((-1, len(feature_labels)))
    data = pd.DataFrame(data = features, index = village_ids, columns = feature_labels)  
    data.to_csv(csv_name)
    return ("Finished writing CSV file {}.".format(csv_name))

def preprocess_garv(garv_data_path): 
    ### dataframe setup for GARV dataset
    df = pd.read_csv(garv_data_path)
    df = df.replace(-9, np.nan)
    # Drop ".0" from census ID 
    df['Census 2011 ID'] = df['Census 2011 ID'].astype(str).str[:-2]
    df['Percentage Electrified'] = (df['Number of Electrified Households']/df['Number of Households'])*100
    df = df.dropna(axis=0, how='any') # drop rows that have NaN values 
    df[~df.index.duplicated(keep=False)]
    return df 