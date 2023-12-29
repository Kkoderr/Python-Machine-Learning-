#to import Numeric python library
import numpy as np;

#some data structure useful for us : 1.numpy array 2.pandas dataframe 3.tensorflow tensor 4.pytorch tensor
#proving frequentist definiton of probabiltiy (P(x) = (lim n->infinty) freq(x)/n))

#total sample size
n = 1000
#getting coin toss results using binomial distribution 
coin_tosses = np.random.binomial(1,0.5,n)
print(coin_tosses)
#counting all the non zero values of the numpy array / or total true value for coin_tosses
frequency_x = np.count_nonzero(coin_tosses)
#np.array.shape -> gives a tuple containing (rows,colummns)
relative_frequency_x = frequency_x/coin_tosses.shape[0]
#printing relative frequency (relative frequency(x) = freq(x)/n)
print(relative_frequency_x)



