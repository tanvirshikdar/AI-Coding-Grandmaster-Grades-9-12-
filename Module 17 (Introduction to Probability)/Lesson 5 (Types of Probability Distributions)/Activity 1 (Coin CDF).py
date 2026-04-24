import scipy.stats as stats

prob = 1 - stats.binom.cdf(6, 10, 0.5)

print("The probability of getting more than 6 heads in 10 coin flips is :", prob)