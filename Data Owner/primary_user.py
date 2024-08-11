import os
import sys
import time
import pickle
import datetime
import pandas as pd
from collections import defaultdict
from sample_data_generator import generate_data
from cipher_engine import encrypt, generate_key, hash_message


class Data_owner:
    def __init__(self, user_id, version):
        self.user_id = str(user_id)
        self.failure_reports = []
        self.encryption_key = None
        self.meta_data = defaultdict(list)
        self.current_version = version
        self.file_count = 1
        
    def check_data(self, path):
        try: get_len = len(os.listdir(path))
        except: sys.exit("No such directory present")
        if get_len: return True
        else: return False

    def push_data(self, cloud_path, data_path, folder):
        if self.check_data(data_path):
            self.encryption_key = generate_key()
            dir_path = cloud_path
            cloud_path =  cloud_path + "\\" + folder
            if not(os.path.exists(cloud_path)): os.mkdir(cloud_path)
            
            for file in os.listdir(data_path):
                data_file = open(data_path+"\\"+file, mode="r", encoding='utf-8')
                plain_text = data_file.read()
                encrypted_text = encrypt(self.encryption_key, plain_text)
                cloud_file = open(cloud_path+"\\"+file, mode="w", encoding='utf-8')
                cloud_file.write(encrypted_text)
                time_stamp = str(datetime.datetime.now())
                file_id = file[:-4]
                hash_text = file_id+str(1)+self.user_id+encrypted_text+time_stamp
                hash_value = hash_message(hash_text)
                self.meta_data[file_id].extend([file_id,str(1),self.user_id,encrypted_text,time_stamp,hash_value])

            self.generate_file_records(dir_path)
            #print("successfully pushed ",len(os.listdir(cloud_path))," file to the cloud.")
            return self.meta_data
            
        else:
            print("No data is available for move to Cloud.")
            return None

    def generate_file_records(self,cloud_path):
        files_id = list(self.meta_data.keys())
        versions = [self.meta_data[ID][1] for ID in files_id]
        users_id = [self.meta_data[ID][2] for ID in files_id]
        encry_texts = [self.meta_data[ID][3] for ID in files_id]
        time_stamps = [self.meta_data[ID][4] for ID in files_id]
        hash_values = [self.meta_data[ID][5] for ID in files_id]
        file_record = {"File_ID": files_id, "Version": versions, "User ID": users_id, "Encrypted Text": encry_texts,
                       "Time Stamp": time_stamps, "Hash Value": hash_values}
        df_file_records = pd.DataFrame(file_record)
        rows, cols = df_file_records.shape
        df_file_records.to_csv(cloud_path+"\\"+"file_records_dir"+"\\"+"file_record_"+str(rows)+"_"+str(self.file_count)+".csv")
        self.file_count += 1
        
    def get_failure_reports(self):
        pass
    
    def reverification(self):
        pass

    



# Number_of_files = int(input("Enter the Number of files: "))
# Curruption_percentage = int(input("Enter percent curruption: "))
# File_size = int(input("Enter size of file(KB): "))
# Dir_name = "data"

if __name__ == "__main__":
#Step_1: sample data generation
    Number_of_files, File_size, Dir_name = sys.argv[1:]
    t1 = time.time()    
    generate_data(int(Number_of_files), int(File_size), Dir_name)
    t2 = time.time()
    #print("Generation Time:",t2-t1)

#step_2: upload encrypted data to the cloud space.
    cloud_path = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Cloud Service Provider"
    data_path = r"D:\User Data\Desktop\User Revokeable Distributed Auditing\Data Owner"+"\\"+Dir_name
    primary_user = Data_owner(user_id=1, version=None)
    meta_data = primary_user.push_data(cloud_path, data_path, folder="first_commit")
    with open(data_path+"\\"+"output.pkl", "wb") as f:
        pickle.dump(meta_data, f)

    
