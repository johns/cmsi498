'''
Jimmy Byrne
J Goocher
John Scott
Jackson Watkins

treatment_suggestion.py

CMSI 498 Assignment 2
Problem 3
Determines the optimal treatment to assign to the patient
that represents the covariates W = 0, M = 0.
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

prob_Y_X_is_0 = 0
prob_Y_X_is_1 = 0
#X=0 obs
evidence = ['0', None, None, '0', '0']
obs_model_cpt = obs_model.predict_proba(evidence)
prob_Y_X_is_0 = prob_Y_X_is_0 + obs_model_cpt[2].parameters[0]['1']
#X=1 obs
evidence = ['1', None, None, '0', '0']
obs_model_cpt = obs_model.predict_proba(evidence)
prob_Y_X_is_1 = prob_Y_X_is_1 + obs_model_cpt[2].parameters[0]['1']
#X=0 exp
evidence = ['0', None, None, '0', '0']
exp_model_cpt = exp_model.predict_proba(evidence)
prob_Y_X_is_0 = (prob_Y_X_is_0 + exp_model_cpt[2].parameters[0]['1']) / 2
#X=1 exp
evidence = ['1', None, None, '0', '0']
exp_model_cpt = exp_model.predict_proba(evidence)
prob_Y_X_is_1 = (prob_Y_X_is_1 + exp_model_cpt[2].parameters[0]['1']) / 2

print("P(Y=1|X=0, W=0, M=0) = ", end='')
print(prob_Y_X_is_0)
print("P(Y=1|X=1, W=0, M=0) = ", end='')
print(prob_Y_X_is_1)
if prob_Y_X_is_0 > prob_Y_X_is_1:
    print("Drug 0 is the optimal treatment for patients where X=0 and M=0")
else:
    print("Drug 1 is the optimal treatment for patients where X=0 and M=0")

evidence_bullet4 = [None, None, None, '0', '0']
obs_model_cpt_bullet4 = obs_model.predict_proba(evidence_bullet4)
print("In the wild, the probability patients where X=0 and M=0 are perscribed the optimal drug is ", end='')
print(obs_model_cpt_bullet4[0].parameters[0]['0'])