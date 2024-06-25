import os
import random

def create_file(file_path):
    with open(file_path, 'w') as file:
        for _ in range(100000):
            random_number = random.randint(1,1000)
            file.write(f"{random_number}\n")


def chunk_files(file_path, chunk_size):
    temp_files = [] #List of all the chunk files
    with open(file_path, 'r') as file: #opens the file to be sorted
        index = 0
        while True:
            numberList = file.readlines(chunk_size) #reads up to chunk size and stores into chunk file
            if not numberList:
                break
            numberList = [int(x.strip()) for x in numberList]#removes newline character
            numberList.sort()
            numberList = [str(x) + '\n' for x in numberList]#converts to string and adds new line character
            temp_file = f"sorted_{index}.txt"
            temp_files.append(temp_file)
            with open(temp_file, 'w') as tempfile:
                tempfile.writelines(numberList)#writes the chunk to chunk file
            
            index += 1
            
    return temp_files

def merge_sorted_files(file_paths, final_path):
    final_file = open(final_path, 'a')
    file_handlers = [open(file, 'r') for file in file_paths] #opens all the files

    #reads the first line from each file and stores them into a list
    current_lines = []
    #creates a dictionary -> number:index so we can keep track which file the number is from
    for i, file in enumerate(file_handlers):
        line = file.readline().strip()
        if line:
            current_lines.append((int(line), i))#appends to a temp list 

    while current_lines:
        current_lines.sort(key=lambda x: x[0]) #sorts the first element in the tuple
        smallest_value, index = current_lines.pop(0) #grabs the first tuple and stores it in variables
        final_file.write(str(smallest_value) + '\n') #append the smallest number to sorted file

        #grabs the next number from file we just took the smallest value from
        next_line = file_handlers[index].readline().strip()
        if next_line:
            current_lines.append((int(next_line), index))
    
    for file in file_handlers:#closes all the files
        file.close()
    final_file.close()

create_file("numbers.txt")

input_file_path = "numbers.txt"
chunk_size = 10000

temp_files = chunk_files(input_file_path, chunk_size)

merge_sorted_files(temp_files, "sorted.txt")