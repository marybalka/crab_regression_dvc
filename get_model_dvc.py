# -*- coding: utf-8 -*-



import numpy as np
#import pandas as pd
#import random as rnd
from collect_data_dvc import dataaa


def preprocessing(dataframe, target_variable = 'Age', tt_split = 4/5):
    
    def normalize(dataframe): 
        normalized_dataframe = (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())
        
        return normalized_dataframe
    
    xs = normalize(dataframe.drop([target_variable], axis = 1))
    ys = dataframe.loc[:, target_variable]
    
    split_point = round(len(xs)*tt_split)
    
    xs_train, xs_test = xs.iloc[:split_point], xs.iloc[split_point:]
    ys_train, ys_test = ys.iloc[:split_point], ys.iloc[split_point:]
    
    return xs_train, xs_test, ys_train, ys_test


def develope_model(xs, ys, n_steps, alpha, theta = None):
    
    
    def loss(theta, x, y):
        return (sum(theta*x) - y) 
    
    
    def from_row_to_loss(theta, argument, target):
        
        argument = argument.to_numpy()
        x = np.concatenate((np.array([1]), argument))
        y = target
        
        return loss(theta, x, y) * x
    
    
    if not theta:
        theta = np.zeros(len(xs.iloc[0]) + 1)
        
    n_xs = len(xs.index)
    
    for _ in range(n_steps):
        theta = theta - alpha / n_xs * sum(from_row_to_loss(theta, xs.iloc[k], ys.iloc[k]) for k in range(n_xs)) 
        
    return theta


def accuracy_score(xs, ys, theta):

    return sum(abs(sum(np.concatenate((np.array([1]), xs.iloc[k])) * theta) - ys.iloc[k]) ** 2 for k in range(len(xs.index))) / len(xs.index)


xs_train, xs_test, ys_train, ys_test = preprocessing(dataaa, 'Age')
thetaa = develope_model(xs_train, ys_train, 20, 0.05)
accuracy = accuracy_score(xs_test, ys_test, thetaa)

print(thetaa)
print(accuracy)
