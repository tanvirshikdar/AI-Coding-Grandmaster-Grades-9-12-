# 1. Define the folder path once to keep the code clean
folder_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 2 (Operations on a File – Part 1)\Activity 3 (Remove Lines)"

# 2. Combine folder path with specific file names
input_path = folder_path + r"\Codingal.txt"
output_path = folder_path + r"\CodingalUpdated.txt"

# 3. Open the original file to read and the new file to write
file1 = open(input_path, 'r')
file2 = open(output_path, 'w')

print("--- Lines that do NOT start with 'Coding' ---")

# 4. Process the lines
for line in file1.readlines():
    
    # Check if the line does NOT start with "Coding"
    if not (line.startswith('Coding')):
        
        # Printing those lines to the terminal
        print(line.strip()) # strip() removes extra empty lines in terminal
        
        # Writing those lines to the updated file
        file2.write(line)

# 5. Close and save the files
file2.close()
file1.close()

print("\nTask complete! Check CodingalUpdated.txt for the results.")