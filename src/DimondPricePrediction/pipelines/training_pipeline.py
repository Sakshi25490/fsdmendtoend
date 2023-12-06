from src.DimondPricePrediction.componets.data_ingestion import DataIngestion

import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customeception
import padas as pd


obj=DataIngestion()

obj.initiate_data_ingestion()
