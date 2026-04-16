file_read = open(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\Activity 2 (File Handling Operation - Part 2)\Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\Activity 2 (File Handling Operation - Part 2)\Codingal.txt', 'w')

file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()

file_append = open(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\Activity 2 (File Handling Operation - Part 2)\Codingal.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()