file = open(r'C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\Activity 3 (Lines in File)\Codingal.txt', 'r')
Counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1
        
print("This is the number of lines in the file")
print(Counter)