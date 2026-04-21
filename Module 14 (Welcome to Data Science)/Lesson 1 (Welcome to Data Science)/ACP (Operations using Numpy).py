import numpy as np

original_array = np.linspace(0, 9, 10, dtype=int)
print("Original Array:")
print(original_array)

modified_array = np.where(original_array % 2 != 0, -1, original_array)
print("\nModified Array (Odds replaced with -1):")
print(modified_array)

two_d_array = original_array.reshape(2, 5)
print("\n2D Array (Two rows):")
print(two_d_array)

even_sum = 0
for x in original_array:
    if x % 2 == 0:
        even_sum += x

print(f"\nSum of all even numbers: {even_sum}")