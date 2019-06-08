import gym
import numpy as np
import util
import pickle
import time
import random

env=gym.make('MountainCar-v0')
env.reset()

Q=util.Counter()

def getQValue(x,v,a):
    pass

def Value(x,v):
    pass

def getActions(x,v):
    pass

def getBestAction(x,v,epsilon):
    pass

def update(x,v,a,xn,vn,r,gamma,alfa):
    pass
    


def QLearning(env,alfa,epsilon,gamma,episodes):
        
    de=10**(-3.0/episodes)
    for i in range(episodes):
        cnt=0
        rew=0
        epsilon*=de
        while True:
            
            if i>episodes-20:
                env.render()
            # CODE HERE #
            cnt+=1
            rew+=reward

            if done:
                rewlist.append(rew)
                
                break
        if(i+1)%100==0:
            print("Average Reward for ["+str(i-99)+"..."+str(i)+"]= "+str(np.mean(rewlist)))
            rewlist=[]
            
    with open('dict2.pk','wb') as f:
        pickle.dump(Q,f)
        f.close()
    f=open('dict2.txt','w')
    f.write(str(Q))
    f.close()

def Play(env,episodes):
    

    for i in range(episodes):
        
        rew=0
        cnt=0
        # CODE HERE #
        while True:
            
            env.render()
            cnt+=1
            rew+=reward
            if done and cnt<200:
                print("iteration "+str(i+1)+": WIN\tReward: "+str(rew))
                break
            if done:
                print("iteration "+str(i+1)+": LOSE.\tReward: "+str(rew))
                break


QLearning(env,0.2,0.8,0.9,5000)
Play(env,10)
env.close()
        
        
        
        

        

        
