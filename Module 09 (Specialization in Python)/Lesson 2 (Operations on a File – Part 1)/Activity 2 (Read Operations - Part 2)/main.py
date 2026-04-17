file_path = r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 2 (Operations on a File – Part 1)\Activity 2 (Read Operations - Part 2)\Codingal.txt'

file_read = open(file_path, 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open(file_path, 'w')
file_write.write("File in write mode ....\n")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()

file_append = open(file_path, 'a')
file_append.write("\nFile in append mode ....")
file_append.write("\nHi! I am Penguin. I am 1 yr. old")
file_append.close()