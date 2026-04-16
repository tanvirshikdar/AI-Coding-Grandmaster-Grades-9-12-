import os

sample_file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\ACP (File Handling - Operations Part 2)\Sample_File.txt"
my_file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\ACP (File Handling - Operations Part 2)\My_file.txt"
sample_doc_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\ACP (File Handling - Operations Part 2)\Sample_doc.txt"

with open(sample_file_path, 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")

with open(sample_file_path, 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)

print("\nChecking if my_file exists or not....")
if os.path.exists(my_file_path):
    print("File exists")
else:
    print("The file does not exist")

my_file = open(my_file_path, "w")
my_file.write("Hi! I am Penguin. I am in class 8 studying in Pune.")
my_file.close()

if os.path.exists(sample_doc_path):
    os.remove(sample_doc_path)
    print("Sample_doc.txt deleted successfully.")
else:
    print("Sample_doc.txt not found, so it couldn't be deleted.")