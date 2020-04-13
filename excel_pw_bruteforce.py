#WRITTEN BY: ALI ALNUAIMI ~ https://www.linkedin.com/in/ali-alnuaimi-9847a1164/
#USAGE:
    #1- CMD: Enter the folder where this script is located
    #2- CMD: Type "excel_pw_bruteforce.py" and follow the instructions
#REQUIREMENTS: Below libraries to be installed "pip install <lib_name>"
#NOTES: FOR EDUCATION PURPOSES ONLY

import tempfile, shutil, os
import random
from win32com.client import Dispatch



def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, str(random.randint(1, 100000)) + 'temp_file_name.xlsx')
    shutil.copy2(path, temp_path)
    return temp_path

def find_password():
    print ("Starting ...")

    instance = Dispatch('Excel.Application')
    temp_file = create_temporary_copy(file)

    for pw in password_list:
        try:
            print("Attempting: " + pw.strip())
            instance.Workbooks.Open(temp_file, False, True, None, pw.strip())
            print ("Password Found!: " + pw.strip())
            print ("Stopping...")
            break
        except:
            pass
    try:
        instance.Workbooks.Close(SaveChanges = 0)
    except:
        pass
    instance.Quit()

    os.remove(temp_file)


file = ""
password_list = []

if __name__ == '__main__':
    while True:
        input1 = input('File to bruteforce (.xlsx): ')
        if (input1.split(".")[-1] == "xlsx" and os.path.exists(input1)):
            file = input1
            break
        else:
            print ("File type not supported or file doesn't exist")


    while True:
        input2 = input('Wordlist (.txt): ')
        if (input2.split(".")[-1] == "txt" and os.path.exists(input2)):
            password_list = open(input2,'r').read().splitlines()
            break
        else:
            print ("File type not supported or file doesn't exist")


    find_password()
