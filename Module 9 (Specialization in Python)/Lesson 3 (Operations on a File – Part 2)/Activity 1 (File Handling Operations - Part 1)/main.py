file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 1 (File Handling Operations - Part 1)\Codingal.txt"

with open(file_path, 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")

with open(file_path, 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)