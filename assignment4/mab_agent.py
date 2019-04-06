'''
Jimmy Byrne
J Goocher
John Scott
Jackson Watkins

mab_agent.py

CMSI 498 Assignment 4
Agent specifications implementing Action Selection Rules.
'''

import random
import numpy as np

# ----------------------------------------------------------------
# MAB Agent Superclasses
# ----------------------------------------------------------------

class MAB_Agent:
    '''
    MAB Agent superclass designed to abstract common components
    between individual bandit players (below)
    '''

    def __init__ (self, K):
        # TODO: Placeholder: add whatever you want here
        self.K = K
        self.history = [[], [], [],[]]

    def give_feedback (self, a_t, r_t):
        '''
        Provides the action a_t and reward r_t chosen and received
        in the most recent trial, allowing the agent to update its
        history
        '''
        self.history[a_t].append(r_t)

    def clear_history(self):
        '''
        IMPORTANT: Resets your agent's history between simulations.
        No information is allowed to transfer between each of the N
        repetitions
        '''
        self.history = [[], [], [], []]


# ----------------------------------------------------------------
# MAB Agent Subclasses
# ----------------------------------------------------------------

class Greedy_Agent(MAB_Agent):
    '''
    Greedy bandit player that, at every trial, selects the
    arm with the presently-highest sampled Q value
    '''

    def __init__ (self, K):
        MAB_Agent.__init__(self, K)

    def choose (self, *args):
        ad_values = []
        for ad in self.history:
            cumulative_reward = sum(ad)
            n = len(ad)
            if n == 0 :
                ad_values.append(1)
            else:
                ad_values.append(cumulative_reward/n)

        return ad_values.index(max(ad_values))


class Epsilon_Greedy_Agent(MAB_Agent):
    '''
    Exploratory bandit player that makes the greedy choice with
    probability 1-epsilon, and chooses randomly with probability
    epsilon
    '''

    def __init__ (self, K, epsilon):
        MAB_Agent.__init__(self, K)
        self.epsilon = epsilon

    def choose (self, *args):
        if random.uniform(0, 1) < self.epsilon:
            return np.random.choice(list(range(self.K)))

        ad_values = []
        for ad in self.history:
            cumulative_reward = sum(ad)
            n = len(ad)
            if n != 0 :
                ad_values.append(cumulative_reward/n)
            else:
                ad_values.append(1)

        return ad_values.index(max(ad_values))


class Epsilon_First_Agent(MAB_Agent):
    '''
    Exploratory bandit player that takes the first epsilon*T
    trials to randomly explore, and thereafter chooses greedily
    '''

    def __init__ (self, K, epsilon, T):
        MAB_Agent.__init__(self, K)
        self.epsilon = epsilon
        self.T = T
        self.numberOfTrials = 0

    def clear_history(self):
        self.history = [[], [], [], []]
        self.numberOfTrials = 0

    def choose (self, *args):
        if self.numberOfTrials < self.epsilon * self.T:
            self.numberOfTrials += 1
            return np.random.choice(list(range(self.K)))

        ad_values = []
        for ad in self.history:
            cumulative_reward = sum(ad)
            n = len(ad)
            if n != 0 :
                ad_values.append(cumulative_reward/n)
            else:
                ad_values.append(1)

        return ad_values.index(max(ad_values))


class Epsilon_Decreasing_Agent(MAB_Agent):
    '''
    Exploratory bandit player that acts like epsilon-greedy but
    with a decreasing value of epsilon over time
    '''

    def __init__ (self, K):
        MAB_Agent.__init__(self, K)
        self.epsilon = .20 # play around with epsilon and decay for better results
        self.decay_rate = .0003

    def clear_history(self):
        self.history = [[], [], [], []]
        self.epsilon = .20

    def choose (self, *args):
        self.epsilon = self.epsilon - self.decay_rate
        if random.uniform(0, 1) < self.epsilon:
            return np.random.choice(list(range(self.K)))

        ad_values = []
        for ad in self.history:
            cumulative_reward = sum(ad)
            n = len(ad)
            if n == 0 :
                ad_values.append(1)
            else:
                ad_values.append(cumulative_reward/n)

        return ad_values.index(max(ad_values))


class TS_Agent(MAB_Agent):
    '''
    Thompson Sampling bandit player that self-adjusts exploration
    vs. exploitation by sampling arm qualities from successes
    summarized by a corresponding beta distribution
    '''

    def __init__ (self, K):
        MAB_Agent.__init__(self, K)

    def choose (self, *args):
        ad_beta_values = []
        for ad in self.history:
            wins = sum(ad)
            losses = len(ad) - sum(ad)
            if wins == 0 or losses == 0:
                ad_beta_values.append(1)
            else:
                ad_beta_values.append(np.random.beta(wins, losses))

        return ad_beta_values.index(max(ad_beta_values))
