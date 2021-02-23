'''super simulation of slotted aloha- just 7 lines of code'''

from numpy import random as r

def simple_sim(p, steps, num_success = 0):
   for i in range(steps+1): 
       num_success += int((r.rand() < p) != (r.rand() < p))
   return num_success

(p, steps) = (0.1, 1000000)
print("Throughput = "+str(simple_sim(p,steps)/steps))


