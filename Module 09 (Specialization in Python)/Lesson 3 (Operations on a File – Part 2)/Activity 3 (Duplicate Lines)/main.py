input_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 3 (Duplicate Lines)\Repeated.txt"
output_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 3 (Operations on a File – Part 2)\Activity 3 (Duplicate Lines)\UpdatedFile.txt"

outputFile = open(output_path, "w")
inputFile = open(input_path, "r")

lines_seen_so_far = set()

print("Eliminating duplicate lines....")

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)     

inputFile.close()
outputFile.close()

print("Task complete! Duplicates removed.")