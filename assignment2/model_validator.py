'''
Jimmy Byrne
John Scott
Jackson Watkins

model_validator.py

CMSI 498 Assignment 2
Problem 3
Attempts to validate observational model by comparing queries
in both observational and experimental settings.
'''

import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing, tree
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, KBinsDiscretizer  # noqa: E501
from sklearn.naive_bayes import GaussianNB


COLUMNS = ["X", "Z", "Y", "M", "W"]  # noqa: E501

# reading training and test data
obs_data = pd.read_csv('med_ex_obs.csv', names=COLUMNS)
exp_data = pd.read_csv('med_ex_exp.csv', names=COLUMNS)
