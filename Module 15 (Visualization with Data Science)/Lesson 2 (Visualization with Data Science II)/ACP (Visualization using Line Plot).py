import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

july_data = {
    'Day': [1, 5, 10, 15, 20, 25, 31],
    'Birth_Rate': [45, 52, 48, 60, 55, 65, 58]
}
august_data = {
    'Day': [1, 5, 10, 15, 20, 25, 31],
    'Birth_Rate': [50, 48, 55, 52, 68, 70, 62]
}

df_july = pd.DataFrame(july_data)
df_august = pd.DataFrame(august_data)

plt.figure(figsize=(10, 5))
plt.plot(df_july['Day'], df_july['Birth_Rate'], 
         marker='o', linestyle='--', linewidth=2, color='blue', label='July')
plt.title('Birth Rate - July')
plt.xlabel('Day of Month')
plt.ylabel('Birth Rate')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df_august['Day'], df_august['Birth_Rate'], 
         marker='s', linestyle='-.', linewidth=2, color='green', label='August')
plt.title('Birth Rate - August')
plt.xlabel('Day of Month')
plt.ylabel('Birth Rate')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df_july['Day'], df_july['Birth_Rate'], 
         marker='o', linestyle='-', linewidth=2, color='blue', label='July')
plt.plot(df_august['Day'], df_august['Birth_Rate'], 
         marker='s', linestyle='-', linewidth=2, color='green', label='August')
plt.title('Birth Rate Comparison: July vs August')
plt.xlabel('Day of Month')
plt.ylabel('Birth Rate')
plt.legend()
plt.grid(True)
plt.show()

x = np.arange(1, 11)
y = 6 * (x**2) + x + 1

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='D', linestyle='-', color='red', label='$y = 6x^2 + x + 1$')
plt.title('Linear/Non-Linear Function: $y = 6x^2 + x + 1$')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()
plt.grid(True)
plt.show()