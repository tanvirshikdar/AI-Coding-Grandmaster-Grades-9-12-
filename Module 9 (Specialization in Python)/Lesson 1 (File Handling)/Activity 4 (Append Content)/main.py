firstfile = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\Activity 4 (Append Content)\Codingal.txt"
secondfile = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 1 (File Handling)\Activity 4 (Append Content)\sample_doc.txt"

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('content of first file before appending -\n', f1.read())
print('content of second file before appending - \n', f2.read())

f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('content of first file after appending - \n', f1.read())
print('content of second file after appending - \n', f2.read())

f1.close()
f2.close()