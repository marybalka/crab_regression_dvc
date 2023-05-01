# -*- coding: utf-8 -*-


import pandas as pd
#import random as rnd

import os
import fnmatch
#import re

#creates an array of available dataframes in given directory
def find(path):
    regex = '*.csv'
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, regex):
                result.append(os.path.join(root, name))
    
    return result


#creates an dict-type object which links number of observation to the observed data
def create_crab_data_dict():
    crab_data_by_weeks = {}
    res = find('C:\\Users\\User\\crab')
    for (index, dataframe) in enumerate(res, 1):
        crab_data_by_weeks.update({index: pd.read_csv(dataframe, decimal = '.').iloc[:, 1:]})
                           
    return crab_data_by_weeks


#creates a data-frame from dictionary of observed data and indexes of observations
def get_data(keys, data_dict):
    data = pd.concat([data_dict.get(key) for key in keys], axis = 0)
    
    return data

data_dict = create_crab_data_dict()
dataaa = get_data([1,2,3], data_dict)