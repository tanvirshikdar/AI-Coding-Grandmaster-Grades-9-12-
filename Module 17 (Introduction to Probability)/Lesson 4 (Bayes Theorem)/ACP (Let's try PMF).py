import scipy.stats as stats

prob_1 = stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5)
print("Probability of observing between 2 and 4 heads")
print(prob_1)