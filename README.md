# reinforcement

These are various simulations that incorporate the power of Reinforcement Learning to teach an intelligent agent to act in an environment.

Currently I am working on an agent that will traverse its environment which is a N x N grid.

Legend of the map is as follows:

A - Agent current location
o - Walkable path
g - Goal

The implementation of this simulation is trivial at this point in time. The user can generate an N x N map and choose the location of the goal. The agent learns to traverse the environment to reach the goal with each action or step giving it a reward.

For every non-goal state arrival, the agent gets a reward of -1 :(
Upon arrival at the goal state we grant our agent a generous reward of 100 (100 what? apples?, bananas?, we'll let the agent decide what the unit will be)

The most basic form of this map includes an unobstructed environment which the agent can freely traverse and reach the goal.

In the future there will be many variants. Can't let the agent be a simple maze solver, we need to teach him to travel in style!
I am planning to add more and more obstacles like traps(that can be fatal to the agent, or cause them to be stuck for a while), moving adversaries and much more.

For now I will focus on adding the worst nightmare for an agent traversing in the environment so easily........WALLS!!!!!
