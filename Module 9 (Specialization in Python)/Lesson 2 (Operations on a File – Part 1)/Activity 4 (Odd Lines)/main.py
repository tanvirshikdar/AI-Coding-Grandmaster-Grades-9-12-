folder = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 2 (Operations on a File – Part 1)\Activity 4 (Odd Lines)"

input_file = folder + r"\Codingal.txt"
output_file = folder + r"\CodingalUpdated.txt"

fn = open(input_file, 'r')

fn1 = open(output_file, 'w')

cont = fn.readlines()

for i in range(len(cont)):
    # Check if the line number (i+1) is odd
    if ((i + 1) % 2 != 0):
        fn1.write(cont[i])
    else:
        pass

fn1.close()

fn1 = open(output_file, 'r')
cont1 = fn1.read()

print("--- Contents of Odd Lines (CodingalUpdated.txt) ---")
print(cont1)

fn.close()
fn1.close()