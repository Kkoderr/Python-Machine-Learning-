import numpy as np
from matplotlib import pyplot as plt
sample_size = (1000000,5)
coin_toss = np.random.binomial(1,0.5,sample_size)
desired_outcome_frequency = np.sum(coin_toss,axis=1)
n=0
frequency = list()
while(n!=6):
    frequency.append(np.count_nonzero(desired_outcome_frequency==n))
    #print(np.sum(desired_outcome_frequency==n))
    n+=1
frequency = np.array(frequency)
#relative_frequency = np.divide(frequency,sample_size[0])
relative_frequency = frequency/(np.shape(desired_outcome_frequency))[0]
print(frequency)
print(relative_frequency)
x = np.arange(0,6)
print(x)
plt.bar(x=x,height=relative_frequency)
plt.show()