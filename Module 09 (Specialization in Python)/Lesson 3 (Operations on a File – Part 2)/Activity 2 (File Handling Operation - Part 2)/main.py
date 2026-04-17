import os

folder_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 2 (File Handling Operation - Part 2)"

codingal_file = os.path.join(folder_path, "Codingal.txt")
new_file_path = os.path.join(folder_path, "New_File.txt")
my_file_path = os.path.join(folder_path, "my_file.txt")
test_folder = os.path.join(folder_path, "Folder")

if not os.path.exists(new_file_path):
    new_file = open(new_file_path, 'x')
    print("Created New_File.txt")
    new_file.close()
else:
    print("New_File.txt already exists.")

print("Checking if my_file exists or not....")
if os.path.exists(my_file_path):
    os.remove(my_file_path)
    print("Old my_file.txt removed.")
else:
    print("The file does not exist")

my_file = open(my_file_path, "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()
print("Created and wrote to my_file.txt")

if os.path.exists(codingal_file):
    os.remove(codingal_file)
    print("Codingal.txt deleted.")
else:
    print("Codingal.txt not found, skipping deletion.")

if os.path.exists(test_folder):
    os.rmdir(test_folder)
    print("Folder deleted.")
else:
    print("Folder not found.")