import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

july_data = {
    'Weeks': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
    'Birth_Rate': [120, 150, 130, 170]
}
august_data = {
    'Weeks': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
    'Birth_Rate': [140, 160, 125, 180]
}

df_july = pd.DataFrame(july_data)
df_august = pd.DataFrame(august_data)

plt.figure(figsize=(8, 5))
plt.bar(df_july['Weeks'], df_july['Birth_Rate'], color='skyblue', width=0.5, edgecolor='navy')
plt.title('Birth Rate - July')
plt.xlabel('Weeks')
plt.ylabel('Birth Rate')
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(df_august['Weeks'], df_august['Birth_Rate'], color='salmon', width=0.5, edgecolor='red')
plt.title('Birth Rate - August')
plt.xlabel('Weeks')
plt.ylabel('Birth Rate')
plt.show()

plt.figure(figsize=(10, 6))
x = np.arange(len(df_july['Weeks']))
width = 0.35

plt.bar(x - width/2, df_july['Birth_Rate'], width, label='July', color='skyblue', edgecolor='navy')
plt.bar(x + width/2, df_august['Birth_Rate'], width, label='August', color='salmon', edgecolor='red')

plt.title('Birth Rate Comparison: July vs August')
plt.xlabel('Weeks')
plt.ylabel('Birth Rate')
plt.xticks(x, df_july['Weeks'])
plt.legend()
plt.show()