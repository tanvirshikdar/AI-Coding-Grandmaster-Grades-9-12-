import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

matches_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 18 (Machine Learning - I)\Lesson 2 (Understanding more about data)\ACP (Data preprocessing)\matches.csv"
deliveries_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 18 (Machine Learning - I)\Lesson 2 (Understanding more about data)\ACP (Data preprocessing)\deliveries.csv"

matches = pd.read_csv(matches_path)
deliveries = pd.read_csv(deliveries_path)

print("--- Matches Dataset Info ---")
print(matches.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(matches.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title("Null Values in Matches")
plt.show()

if 'umpire3' in matches.columns:
    matches.drop('umpire3', axis=1, inplace=True)

matches.dropna(inplace=True)
print("Matches cleaned. Current shape:", matches.shape)


print("\n--- Deliveries Dataset Info ---")
print(deliveries.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(deliveries.isnull(), yticklabels=False, cbar=False, cmap='magma')
plt.title("Null Values in Deliveries")
plt.show()

unwanted_cols = ['player_dismissed', 'dismissal_kind', 'fielder']
deliveries.drop(columns=[col for col in unwanted_cols if col in deliveries.columns], inplace=True)

deliveries.dropna(inplace=True)
print("Deliveries cleaned. Current shape:", deliveries.shape)


print("\n--- Merging Datasets ---")
matches.rename(columns={'id': 'match_id'}, inplace=True)

merged_data = pd.merge(deliveries, matches, on='match_id')

print("Final Merged Dataset Preview:")
print(merged_data.head())
print(f"\nFinal Dataset Shape: {merged_data.shape}")

sns.heatmap(merged_data.isnull(), cbar=False)
plt.title("Final Cleaned Dataset")
plt.show()