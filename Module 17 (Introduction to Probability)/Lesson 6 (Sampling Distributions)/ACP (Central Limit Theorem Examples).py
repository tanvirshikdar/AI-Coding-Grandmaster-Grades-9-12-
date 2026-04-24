import numpy as np
import matplotlib.pyplot as plt

def run_clt_simulation(data, title, subplot_pos):
    sample_means = []
    
    for _ in range(1000):
        sample = np.random.choice(data, size=30, replace=True)
        sample_means.append(np.mean(sample))
    
    plt.subplot(2, 3, subplot_pos)
    plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black')
    plt.title(title, fontsize=10)
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')

plt.figure(figsize=(15, 10))

die_rolls = np.random.randint(1, 7, 10000)
run_clt_simulation(die_rolls, "1. Dice Rolls (Ludo)", 1)

coin_flips = np.random.binomial(1, 0.5, 10000)
run_clt_simulation(coin_flips, "2. Coin Flips", 2)

wait_times = np.random.exponential(scale=5, size=10000)
run_clt_simulation(wait_times, "3. Restaurant Wait Times", 3)

income = np.random.pareto(3, 10000)
run_clt_simulation(income, "4. Annual Income", 4)

pets = np.random.poisson(lam=2, size=10000)
run_clt_simulation(pets, "5. Pets per Household", 5)

plt.tight_layout()
plt.show()