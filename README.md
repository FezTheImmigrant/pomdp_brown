# Markvov Decision Process on 2D Grid World
## Description
This application calculates the optimal policy of an agent moving through a 2D grid world using Bellman's Optimal Equation,
otherwise known as value iteration. Users can configure various aspects of the grid world, namely row size, column size,
reward value, lambda value, wall locations, end states, and stochasticity.
The application was written in python, and a link to the docker hub repository can be found [here](https://hub.docker.com/repository/docker/feztheimmigrant/pomdp_brown).
The link provides more information on how to run the application using docker.

## How To Install
The source code can be installed using the following command:
```
git clone https://github.com/FezTheImmigrant/pomdp_brown 
```
## How To Run
### Dependencies
Before running, you need to have the following dependencies installed:
- python 3.8
- numpy
- tabulate

Once the dependencies are installed you can run the application with the following command
```
python3 gridworld.py
```
## How To Use
When users run the application, a main menu will open up with three options:
- 1. Compute Optimal MDP policy.
    - Run Bellman's Optimal Equation for N iterations.
- 2. Reset grid world.
    - Reset the grid world policy and utility to their initial states.
- 3. Quit.
    - Exit the application.
### Configuring Grid World
Here is an example configuration file that would be ingested by the application:
```
{
  "Rows": 3,
  "Columns": 4,
  "Reward": 2,
  "Lambda": 1.0,

  "probabilities": {
    "cw_0": 0.8,
    "cw_90": 0.1,
    "cw_180": 0,
    "cw_270": 0.1
  },

  "Walls": [
    [1,1]
  ],
  "EndStates":[
    [0,3],
    [1,3]
  ],
  "EndStateRewards":[
    1,
    -1
  ]
}
```
It is worth clarifying the "probabilities" section of this configuration file. As mentioned in the description section above, the application allows users to add stochasticity to their grid world environment. The "cw_XX" fields do just that:
- 'cw_0' allows the user to add a probability of how likely an agent is going to move in its intended direction.
- 'cw_90' allows the user to add a probability of how likely an agent is going to move 90 degrees clockwise from its intended direction.
- 'cw_180' allows the user to add a probability of how likely an agent is going to move 180 degrees clockwise from its intended direction.
- 'cw_270' allows the user to add a probability of how likely an agent is going to move 270 degrees clockwise from its intended direction.

## Credits
I credit my work on this application to the professors in the Computer Science department at Brown University, namely Professor Stefanie Tellex and Professor Michael Littman. Additionally, I credit my work on this application to Professor Charles Isbell for his work alongside Professor Littman to create the tutorial series "Machine Learning by Georgia Tech" on Udacity, which was critical to my understanding of Markov Decision Processes.
