import matplotlib.pyplot as plt
import numpy as np

#Data set that can be worked
#EG AB Testing hypothesis under the null hypothesis i.e. there is no difference
#Thats why we use the same probability

p = 0.10 #probability of e.g. conversion
n_new = 15000 #number of customers receiving experiment
n_old = 17000 #number of customers receiving control
experiment = np.random.binomial(n_new, p, size=10000)/n_new
control = np.random.binomial(n_old, p, size=10000)/n_new
diffs = experiment - control #Difference in means in 10k iterations
obs_difference = 0.02 #Assume we see a 2% difference between experiment and control

#whats the probability of the 2% we saw happening if the null hypothesis is true?

plt.hist(diffs)
plt.title("distribution under the null")
plt.axvline(x=np.percentile(diffs,2.5),color='green') #Will provide the 2.5% lower boundry for alpha = 0.05
plt.axvline(x=np.percentile(diffs,97.5),color='green') #will provide the 2.5% upper boundry
plt.axvline(x=np.mean(diffs),color='w') #provides the mean of the distribution in white
plt.axvline(x=obs_difference,color='r') # visualizes the observed difference. If it is outside the green boundaries, you can reject the isnull
