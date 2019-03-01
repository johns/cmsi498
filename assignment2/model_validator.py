'''
Jimmy Byrne
J Goocher
John Scott
Jackson Watkins

model_validator.py

CMSI 498 Assignment 2
Problem 3
Attempts to validate observational model by comparing queries
in both observational and experimental settings.
'''

import pandas as pd
from pomegranate import BayesianNetwork

COLUMNS = ["X", "Z", "Y", "M", "W"]

# Reading training and test data
obs_data = pd.read_csv('med_ex_obs.csv', names=COLUMNS)
exp_data = pd.read_csv('med_ex_exp.csv', names=COLUMNS)

obs_model = BayesianNetwork.from_samples(obs_data, name='obs_trained_bn', state_names=['X', 'Z', 'Y', 'M', 'W'])
exp_model = BayesianNetwork.from_samples(exp_data, name='exp_trained_bn', state_names=['X', 'Z', 'Y', 'M', 'W'])

prob_W_is_1_obs = .5936
prob_W_is_1_exp = .6021

# Computing query on observational model
evidence = ['0', None, None, None, '0']
prob_W_evidence = [None, None, None, None, '0']
summation = 0
print("Observational dataset:")
for o in range(2):
    print("P(Y=1|do(X={}) = ".format(o), end='')
    evidence[0] = str(o)
    summation = 0
    for p in range(2):
        evidence[4] = str(p)
        prob_W_evidence[4] = str(p)
        obs_model_cpt = obs_model.predict_proba(evidence)
        prob_of_y = obs_model_cpt[2].parameters[0]['1']
        if p == 1:
            summation = summation + prob_of_y * prob_W_is_1_obs
        else:
            summation = summation + prob_of_y * (1 - prob_W_is_1_obs)
    print(summation)

# Computing query on experimental model
evidence = ['0', None, None, None, '0']
prob_W_evidence = [None, None, None, None, '0']
summation = 0
print("\nExperimental dataset:")
for o in range(2):
    print("P(Y=1|do(X={}) = ".format(o), end='')
    evidence[0] = str(o)
    summation = 0
    for p in range(2):
        evidence[4] = str(p)
        prob_W_evidence[4] = str(p)
        exp_model_cpt = exp_model.predict_proba(evidence)
        prob_of_y = exp_model_cpt[2].parameters[0]['1']
        if p == 1:
            summation = summation + prob_of_y * prob_W_is_1_exp
        else:
            summation = summation + prob_of_y * (1 - prob_W_is_1_exp)
    print(summation)
