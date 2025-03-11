#create a file
new_file = open('New_file.txt', 'x')
new_file.close()

#check if the file exists
import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
#create a new if it doesn't 
my_file = open('my_file.txt', 'w')
my_file.write("Hi! I am penguin and I am 1 year old.")
my_file.close()
#delete the file
os.remove('Codingal.txt')
#delete the folder
os.rmdir('Folder')