'''Simulation of p-persistent Slotted Aloha'''

from numpy import random
import matplotlib.pyplot as pt

def run_sim(p, steps):
   '''This function runs a simulation of slotted Aloha. 
      Arguments: 
        p = transmission probability, 
        steps = number of iterations
      Returns:
        outcome = list of outcomes in each slot ('0', '1', or 'X')
        num_success = number of time slots with successful transmissions
   '''
   num_success = 0
   outcome = []
   for i in range(steps):
     t1 = random.rand() < p 
     t2 = random.rand() < p
     if t1 and t2:  #both transmitters transmit
       outcome.append("X")  # a collision happens
     elif (t1 and not(t2)) or (not(t1) and t2): #only one of them transmits
       outcome.append("1")  # a success!
       num_success+= 1 
     else:    #neither transmits
       outcome.append("0") # an idle slot - nothing happened

   return outcome, num_success   #list of outcomes and number of successes

def multi_sim(num_values, steps):
   '''This function runs simulation for p ranging from 0 to 1
      then plots the resulting throughput as a function of p.
      Arguments:
         num_values = number of p values to consider  
         steps = how many iterations to simulation for each p value
      Returns:
         nothing - just plots to a matplotlib figure.
   ''' 
   p_values = []
   tp_values = []
   for i in range(num_values+1):
      p = i/num_values
      num_successes = run_sim(p, steps)[1]
      throughput = num_successes / steps #fraction of times success happened
      print(p, throughput)
      p_values.append(p)
      tp_values.append(throughput)
   pt.plot(p_values, tp_values)
   pt.show()


if __name__ == "__main__":
   #print(run_sim(0.9, 20))
   multi_sim(10, 1000) 
