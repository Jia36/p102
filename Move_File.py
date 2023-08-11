import os
import shutil

from_dir = '/Users/family/Downloads'
to_dir = '/Users/family/Documents'
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extention = os.path.splitext(file_name)
    print(name)
    print(extention)
    if(extention==""):
        continue
    if(extention in ['.txt','.doc','.docx','.pdf']):
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Documents"
        path3 = to_dir + '/' + "Documents" + '/' + file_name
        print("path1 ",path1)
        print("path3 ",path3)
        if os.path.exists(path2):
            print("Moving "+ file_name +"......")
            shutil.move(path1,path3)
            
        else:
            os.makedirs(path2)
            print("Moving "+ file_name +"......")
            shutil.move(path1,path3)