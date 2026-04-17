# 1. Define the absolute path so the file goes to the exact right folder
file_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\ACP (File Handling - Access Modes)\Sample_File.txt"

# 2. OPEN IN WRITE MODE (This creates the file if it doesn't exist)
file_write = open(file_path, 'w')
file_write.write("File in write mode ....\n")
file_write.write("Hi! I am Penguin. I am a class 8 student from Pune\n")
file_write.close()

# 3. OPEN IN APPEND MODE (This adds to the end of the file)
file_append = open(file_path, 'a')
file_append.write("File in append mode ....\n")
file_append.write("Hi! My favourite subject is Mathematics\n")
file_append.close()

# 4. OPEN IN READ MODE (Now we read the final result and print it)
file_read = open(file_path, 'r')
print("--- Final File Contents ---")
print(file_read.read())
file_read.close()