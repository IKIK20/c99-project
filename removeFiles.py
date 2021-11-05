import os
import shutil 
import time

path=input("enter name of directory to be stored:-")
days= time.time()
seconds = time.time() - (days * 24 * 60 * 60)

list_of_files=os.listdir(path)

for file in list_of_files:
    if os.path.exists(path):
        os.walk(path)
        
