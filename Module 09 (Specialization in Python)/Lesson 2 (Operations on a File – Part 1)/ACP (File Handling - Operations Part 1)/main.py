file_path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 2 (Operations on a File – Part 1)\ACP (File Handling - Operations Part 1)\Sample_File.txt'

file = open(file_path, 'r')
print("--- Full Content ---")
print(file.read())
file.close()

file = open(file_path, 'r')
print("\n--- Read in parts (8 chars) ---")
print(file.read(8))
file.close()

file = open(file_path, 'r')
print("\n--- Reading first line ---")
print(file.readline())
file.close()
file = open(file_path, 'r')
print("\n--- Reading multiple lines ---")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
file.close()

file = open(file_path, 'r')
print("\n\n--- Looping through the lines ---")
for line in file:
    print(line.strip()) 
file.close()