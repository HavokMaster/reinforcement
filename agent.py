import os
import numpy as np
import time
n = 5
map = [['o'] * n for i in range(n)]
map[n-1][n-1] = 'g'
#actions = [up, down, left, right]
actions = [0, 1, 2, 3]

#Initializing q_learning parameters
q_table = np.zeros((len(map), len(map[0]), len(actions)))
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1
min_exploration_rate = 0.01
decay_rate = 0.990


def get_goal():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'g':
                return [i, j]

def get_state(state, action):
    row, col = state
    if action == 0 and row-1 >= 0:
        row -= 1
    elif action == 1 and row+1 < n:
        row += 1
    elif action == 2 and col-1 >= 0:
        col -= 1
    elif action == 3 and col+1 < n:
        col += 1
    return [row, col]

def get_reward(state):
    row, col = state
    return 100 if map[row][col] == 'g' else -1
def render(state):
    temp = [row.copy() for row in map]
    row, col = state
    temp[row][col] = 'A'
    for x in temp:
        for y in x:
            print(y, end=' ')
        print()

def aiplay(state, max_actions):
    print("starting ")
    actionsTaken = 0
    possibleActions = {0:"Up", 1:"Down", 2:"Left", 3:"Right"}
    time.sleep(2)
    os.system('cls')
    render(state)
    while(actionsTaken < max_actions):
        time.sleep(2)
        os.system('cls')
        action = np.argmax(q_table[state[0], state[1], :])
        print("Best actions seems to be....", possibleActions[action], '\n')
        state = get_state(state, action)
        render(state)
        if state == get_goal():
            print("Agent reached the goal!")
            return
        

def train(episodes):
    global exploration_rate
    max_steps = n*n
    for episode in range(episodes):
        state = [0, 0]
        done = False
        steps = 0
        while not done:
            row, col = state
            if np.random.rand() < exploration_rate:
                action = np.random.choice(actions)
            else:
                action = np.argmax(q_table[row, col, :])
            
            new_state = get_state(state, action)
            reward = get_reward(state)

            q_table[row, col, action] = (1-learning_rate)*q_table[row, col, action] + learning_rate*(
                reward + discount_factor*(max(q_table[new_state[0], new_state[1], :]))
            )
            
            state = new_state
            steps += 1

            if(state == get_goal() or steps >= max_steps): done = True
        exploration_rate = max(min_exploration_rate, exploration_rate*decay_rate)

train(5000)

aiplay([3,1], 10)