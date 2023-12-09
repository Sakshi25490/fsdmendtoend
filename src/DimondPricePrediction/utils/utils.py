import os 
import sys
import pickle
import numpy as np
import pandas as pd
from srs.DimondPricePrediction.logger import logging
from srs.DimondPricePrediction.Exception import customexception

from sklearn.matrics import r2_score, mean_absolute_error,mean_squared_error


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makdirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise customexception(e,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            #Train model
            model.fit(X_train,y_train)