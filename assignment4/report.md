#  Assignment 4: MAB About You
###  Jimmy Byrne, J Goocher, John Scott, and Jackson Watkins


##  Problem 1: The Greedy Player

1.  **Expectations:** in a sentence or two, describe how you expect this agent to perform on the task at hand.
>  TODO

2.  **Sim Results:** run the simulation script with *only* the `Greedy_Agent` (i.e., modify the `agents` list in the simulation configurations), capture the resulting graph, and add it to your report.
>  TODO


##  Problem 2: The *ϵ*-Greedy Player

1.  **Expectations:** in a sentence or two, describe how you expect this agent to perform with values of *ϵ* ∈ {0.05,0.10,0.15}.
>  TODO

2.  **Sim Results:** run the simulation script with 3 separate versions of the `Epsilon_Greedy_Agent`, parameterized by the 3 separate values of *ϵ* mentioned above, capture the resulting graph, and add it to your report.
>  TODO


##  Problem 3: The *ϵ*-First Player

1.  **Expectations:** in a sentence or two, describe how you used knowledge of a finite-time horizon *T* to choose and then test several values of *ϵ*.
>  TODO

2.  **Sim Results:** run the simulation script with 3 separate versions of the `Epsilon_First_Agent`, parameterized by the 3 separate values of *ϵ* that you mentioned above, capture the resulting graph, and add it to your report.
>  TODO


##  Problem 4: The *ϵ*-Decreasing Player

1.  **Expectations:** in a sentence or two, describe how you used simulated annealing to derive a **cooling schedule** for the decrease of *ϵ* over time (feel free to experiment here, and remark on your approach / findings).
>  TODO

2.  **Sim Results:** run the simulation script with 3 separate versions of the `Epsilon_Decreasing_Agent`, parameterized by the 3 separate cooling schedules that you mentioned above (these might be different by starting values of *ϵ*, rate of decrease, etc.), capture the resulting graph, and add it to your report.
>  TODO


##  Problem 5: The Thompson Sampling Player

1.  **Expectations:** in a sentence or two, describe how you used implemented your Thompson Sampling bandit player.
>  TODO

2.  **Sim Results:** run the simulation script with the *best* versions of each of the previous 4 bandit players PLUS your new Thompson Sampling player. Record the graph and results in your report.
>  TODO

3.  **Compare:** Lastly, rerun the simulations with reward signals that are very similar (i.e., ~1 − 2% away from one another), and see how this modification changes the results (to do so, modify the `P_R` list in `mab_sim.py`)
>  TODO

4.  **Reflect:** how did these approaches compare? Comment on the strengths of your Thompson Sampler as it might perform vs. the others if you did *not know* or did *not have* a *finite* time horizon, *T*.
>  TODO
