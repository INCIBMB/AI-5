# AI-5: MoutainCar
Get an under powered car to the top of a hill (top = 0.5 position)

## Observation
|Num	| Observation	| Min	| Max|
| ----|-------------|-----|----|
|0	  |position     |	-1.2|	0.6|
|1	  |velocity	    |-0.07|0.07|

## Actions
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
You can perform a minimal install of `gym` with:

```
pip3 install gym
git clone https://github.com/INCIBMB/AI-5.git
```
