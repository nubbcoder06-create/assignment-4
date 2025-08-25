file1 = open('output.txt', 'w')
user_input = input("enter the text to be added:")
file1.write(user_input + "\n")
print("Data successfully written to the text file")
file1.close()

file1 = open('output.txt' , 'a')
extra_input = input("enter additional text to append to  the file:")
file1.write(extra_input + "\n")
print("data successfully added to the text file")
file1.close()

file1 = open('output.txt', 'r')
reading_lines = file1.readlines()
print("The final contents of the file are:")
i = 0
for line in reading_lines:
    print(line.strip())
file1.close()