from __future__ import division
import random
import decimal


def montypicks(knowsprize=True,*args):
    doors, prize, contestantsfirstpick = args
    if knowsprize:
        if prize == contestantsfirstpick:
            montysreveal = random.choice(list(set(doors) - set([prize])))
        else: montysreveal = (list(set(doors) - 
                                   set([prize]) - 
                                   set([contestantsfirstpick]))[0])
    else: montysreveal = random.choice(list(set(doors) - 
                                            set([contestantsfirstpick])))
    return montysreveal

def montyhall(switch=True,knowsprize=True):
    doors = [1,2,3]
    prize = random.choice(doors)
    contestantsfirstpick = random.choice(doors)
    montysreveal = montypicks(knowsprize,doors,prize,contestantsfirstpick)
    if montysreveal == prize: return 'tossed' 
    elif switch:
        contestantsfinalselection = (list(set(doors) - 
                                          set([montysreveal]) - 
                                          set([contestantsfirstpick]))[0])
    else: contestantsfinalselection = contestantsfirstpick
    if contestantsfinalselection == prize:
        return 'won'

def itermonty(iters=100000,knowsprize=True):
    successes = tosses = 0
    for i in range(iters): 
        result = montyhall(knowsprize = knowsprize)
        if result == 'won': successes += 1
        elif result == 'tossed': tosses += 1
    winrate = decimal.Decimal(str(successes/iters))
    lesstosswinrate = decimal.Decimal(str(successes/(iters-tosses)))
    print "\n           ***** Separate Run of Games *****"
    if not knowsprize: 
        print "Of ", iters, "games,", tosses, "tossed (because Monty unknowingly"
        print "picked the prize), the switch win rate overall was", winrate
        print "and the rate won, given", (iters - tosses), "opportunities to pick"
        print "was", successes, '/', (iters - tosses), 'or', lesstosswinrate
    if knowsprize:    
        print "When switching, since Monty knew where the prize was and didn't"
        print "pick it, the win rate was", successes, '/', iters , 'or' , winrate

def runagain(runs=10,knowsprize=True):
    for i in range(runs):
        knowsprize = not knowsprize
        itermonty(knowsprize = knowsprize)

runagain(runs=2,knowsprize=False)



