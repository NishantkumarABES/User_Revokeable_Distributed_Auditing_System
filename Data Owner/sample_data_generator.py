import os
import time

#Generate n sample files with p% curruption
data_path = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Data Owner"

def build_dir(name):
    try: os.mkdir(data_path+"\\"+name)
    except OSError as error:
        print(error)
    

def generate_data(n_files, size, name):
    build_dir(name)
    
    for file_id in range(0, n_files):
        path = data_path+"\\"+name+"\\"+"file_"+str(file_id)+".txt"
        file = open(path, mode="w", encoding='utf-8')
        file.write("test "*(size*200))

    #print(n_files," files are successfully created")

if __name__ == "__main__":
    t1 = time.time()    
    generate_data(100, 3, 3, "data")
    t2 = time.time()
    #print("Generation Time:",t2-t1)
