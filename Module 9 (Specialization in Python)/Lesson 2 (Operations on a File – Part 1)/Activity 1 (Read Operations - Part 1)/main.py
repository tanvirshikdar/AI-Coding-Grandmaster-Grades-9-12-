path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 2 (Operations on a File – Part 1)\Activity 1 (Read Operations - Part 1)\Codingal.txt'

file = open(path, 'r')
print("--- Full File Content ---")
print(file.read())
file.close()

file = open(path, 'r')
print("\n--- Read in parts (First 8 characters) ---")
print(file.read(8))
file.close()

file = open(path, 'a')
file.write("\nHi! I am Penguin and I am 1 yr old.")
file.close()

file = open(path, 'r')
print("\n--- Content After Appending ---")
print(file.read())
file.close()