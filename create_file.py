import random

file_size = 17*1024*1024*1024
with open("numbers.txt", 'a') as file:
    while file.tell() < file_size:
        file.write(str(random.randint(0,10**9)) + '\n')