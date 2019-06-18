# AI-5: MoutainCar
Get an under powered car to the top of a hill (top = 0.5 position). A car is on a one-dimensional track, positioned between two “mountains”. The goal is to drive up the mountain on the right; however, the car’s engine is not strong enough to scale the mountain in a single pass. Therefore, the only way to succeed is to drive back and forth to build up momentum.

## Observation
The car’s state, at any point in time, is given by a vector containing its horizonal position and velocity. The car commences each episode stationary, at the bottom of the valley between the hills (at position approximately -0.5), and the episode ends when either the car reaches the flag (position > 0.5) or after 200 moves. The track limits are:

|Num	| Observation	| Min	| Max|
| ----|-------------|-----|----|
|0	  |position     |	-1.2|	0.6|
|1	  |velocity	    |-0.07|0.07|

## Actions
At each move, the car has three actions available to it: push left, push right or do nothing, and a penalty of 1 unit is applied for each move taken (including doing nothing). This means that, unless the can figure out a way to ascend the mountain in less than 200 moves, it will always achieve a total “reward” of -200 units.

|Num|	Action|
|-|-|
|0	|push left|
|1	|no push|
|2	|push right|

## Reward
-1 for each time step, until the goal position of 0.5 is reached. There is no penalty for climbing the left hill, which upon reached acts as a wall.

## Starting State
Random position from -0.6 to -0.4 with no velocity.

## Episode Termination
The episode ends when you reach 0.5 position, or if 200 iterations are reached.

## Installation
Run the following commands to install `gym` and get your project files:

```
pip3 install gym
git clone https://github.com/INCIBMB/AI-5.git
```

## Testing
Open python3 and run the following commands

```
import gym
env=gym.make('MountainCar-v0')
env.reset()
```
