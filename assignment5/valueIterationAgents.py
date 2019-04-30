'''
Jimmy Byrne
J Goocher
John Scott
Jackson Watkins

CMSI 498 Assignment 5
'''
# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp
import util

from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """

        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()
        # A Counter is a dict with default 0
        print "current self.values: " + str(self.values) + "\n"
        print "mdp.getStates(): " + str(mdp.getStates()) + "\n"
        print "mdp.getPossibleActions(state): " + \
            str(mdp.getPossibleActions((0, 0))) + "\n"
        print "mdp.getTransitionStatesAndProbs(state, action): " + \
            str(mdp.getTransitionStatesAndProbs((0, 0), "north")) + "\n"
        print "mdp.getReward(state, action, nextState): " + \
            str(mdp.getReward((0, 0), "south", (0, 1))) + "\n"
        print "mdp.isTerminal(state): " + str(mdp.isTerminal((0, 0))) + "\n"

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # for k in range(iterations):
        #     self.values[self.mdp.getReward()] =

        def value_iterate(current_state, k):
            if mdp.isTerminal(current_state):
                # figure out the base case (vsubk)
                self.values[current_state] = (1, "stay")
                return 1.0
            if k > MAX_K_GIVEN_IN_CMD_FIND_HOW_TO_GET_IT:
                return 0

            listOfSummation = []
            for current_action in range(len(mdp.getPossibleActions(current_state))):
                trans_state_and_probs = mdp.getTransitionStatesAndProbs(
                    current_state, mdp.getPossibleActions(current_state)[current_action])
                currentSummation = 0
                for current_transition_state_and_prob in range(len(trans_state_and_probs)):
                    states_and_prob = trans_state_and_probs[current_transition_state_and_prob]
                    prob = states_and_prob[1]
                    next_state = states_and_prob[0]
                    reward = mdp.getReward(
                        current_state, mdp.getPossibleActions(current_state)[current_action], next_state)
                    currentSummation = currentSummation + prob * \
                        (reward + self.discount*value_iterate(next_state, k+1))
                listOfSummation.append(
                    (currentSummation, mdp.getPossibleActions(current_state)[current_action]))
            bestI = 0
            bestSum = 0
            #print "listOfSummation: " + str(listOfSummation)
            for i in range(len(listOfSummation)):
                if listOfSummation[i][0] > bestSum:
                    bestI = i
                    bestSum = listOfSummation[i][0]
            self.values[current_state] = listOfSummation[bestI]
            return listOfSummation[bestI][0]

        average_summation = 0
        for i in range(self.iterations):
            average_summation = average_summation + \
                value_iterate(mdp.getStartState(), k=0) / self.iterations

        value_iterate(mdp.getStartState(), 0)
        print "self.values: " + str(self.values)

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          TODO:
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          TODO:
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
