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
from pomegranate import *


COLUMNS = ["X", "Z", "Y", "M", "W"]  # noqa: E501

# reading training and test data
obs_data = pd.read_csv('med_ex_obs.csv', names=COLUMNS)
exp_data = pd.read_csv('med_ex_exp.csv', names=COLUMNS)

obs_model = BayesianNetwork.from_samples(obs_data, name='obs_trained_bn', state_names=['X', 'Z', 'Y', 'M', 'W'])
exp_model = BayesianNetwork.from_samples(exp_data, name='exp_trained_bn', state_names=['X', 'Z', 'Y', 'M', 'W'])

# evidence = {}
# obs_model_cpt = obs_model.predict_proba(evidence)
# exp_model_cpt = obs_model.predict_proba(evidence)