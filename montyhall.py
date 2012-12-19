import random
import decimal
from __future__ import division

def dumbmontyhall(switch=True):
    doors = [1,2,3]
    prize = random.choice(doors)
    contestantsfirstpick = random.choice(doors)
    montysreveal = random.choice(list(
                set(doors) - 
                set([contestantsfirstpick])))
    if switch:
        contestantsfinalselection = (list(
                set(doors) - 
                set([montysreveal]) - 
                set([contestantsfirstpick]))[0])
    else:
        contestantsfinalselection = contestantsfirstpick
    if contestantsfinalselection == prize:
        return True
    else: 
        return False

def montyhall(switch=True):
    doors = [1,2,3]
    prize = random.choice(doors)
    contestantsfirstpick = random.choice(doors)
    if prize == contestantsfirstpick:
        montysreveal = random.choice(list(
                set(doors) - 
                set([prize])))
    else:
        montysreveal = (list(
                set(doors) - 
                set([prize]) - 
                set([contestantsfirstpick]))[0])
    if switch:
        contestantsfinalselection = (list(
                set(doors) - 
                set([montysreveal]) - 
                set([contestantsfirstpick]))[0])
    else:
        contestantsfinalselection = contestantsfirstpick
    if contestantsfinalselection == prize:
        return True
    else: 
        return False

def itermonty(n=1000000):
    successes = 0
    for i in range(n):
        if montyhall():
            successes += 1
    winper = decimal.Decimal(str(successes/n))
    print 'Monty Hall played {0} times, won prize {1} of the time.'.format(n,winper)
    successes = 0
    for i in range(n):
        if dumbmontyhall():
            successes += 1
    winper = decimal.Decimal(str(successes/n))
    print 'Monty Hall (dumb) played {0} times, won prize {1} of the time.'.format(n,winper)

for i in range(10):
    itermonty()
