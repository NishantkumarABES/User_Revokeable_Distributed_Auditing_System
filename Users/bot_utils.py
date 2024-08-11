# simulating the activity of multiple users accessing the cloud
import os
import time
import shutil
import subprocess
import pandas as pd
import hashlib
from random import sample, randint

def delete_generated_data(dir_path):
     shutil.rmtree(dir_path)

def hash_message(message):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode())
    return sha256_hash.hexdigest()

def verify_hash(message, hash_value):
    return hash_message(message) == hash_value


data_owner_path = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Data Owner\primary_user.py"
cloud_path = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Cloud Service Provider\first_commit"
data_path = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Data Owner\data"

def upload_data(path,n_files, size, dir_name):
    # Data owner upload the files to CSP
    result = subprocess.run(["python",path,str(n_files),str(size),dir_name], capture_output=True, text=True)
    #print(result.stdout)
    #print(result.stderr)


def manual_corruption(per_corruption, n_files, path, file_record_dir):
    # Manually corruption of files at cloud
    n_corrupt = (per_corruption*n_files)//100
    corrupted_files = sample(range(n_files),n_corrupt)
    file_record_path = file_record_dir + "\\" + "file_record_"+str(n_files)+"_"+str(1)+".csv"
    #file_count = file_count + 1
    file_record = pd.read_csv(file_record_path)
    for file_id in corrupted_files:
        file_ID = "file_"+str(file_id)
        file = open(cloud_path+"\\"+file_ID+".txt", mode="a", encoding='utf-8')
        updated_text = "corrupted_data "*randint(5,20)
        index = file_record[file_record["File_ID"]==file_ID].index[0]
        file_record.at[index,"Encrypted Text"] = file_record["Encrypted Text"][index] + updated_text
        file.write(updated_text)
        

    #print(n_corrupt,"Files are corrupted at cloud manually.\n")
    
# Sequentially reading every file.
# Bot has reading access of every file.


failure_reports_dir = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Data Owner\failure_reports"

     

#upload_data(data_owner_path,1000,2,"data")
     



          

          
         
    
    



    
    
    
    




