file1_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 4 (File Merge)\Codingal.txt"
file2_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 4 (File Merge)\sample_doc.txt"
merged_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 4 (File Merge)\MergedFile.txt"

with open(file1_path, 'r') as fp:
    data1 = fp.read()

with open(file2_path, 'r') as fp:
    data2 = fp.read()

print("Merging two files....")
data_final = data1 + "\n" + data2

with open(merged_path, 'w') as fp:
    fp.write(data_final)

print("Task complete! Check MergedFile.txt to see the results.")