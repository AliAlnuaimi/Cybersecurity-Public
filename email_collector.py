#WRITTEN BY: ALI ALNUAIMI ~ https://www.linkedin.com/in/ali-alnuaimi-9847a1164/

#INTRO: Use to scan a txt file for email addresses and Prints out a list of emails found.

#USAGE:
    #1- CMD: Enter the folder where this script is located
    #2- CMD: Type "email_collector.py" and provide the txt file

#REQUIREMENTS: Below libraries to be installed "pip install <lib_name>" if not already

#NOTES: FOR EDUCATION PURPOSES ONLY


import os.path
import re
from optparse import OptionParser

def find_emails(s):
    regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                        "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                        "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

if __name__ == '__main__':
    f = ""
    while True:
        input1 = input('Data file (txt): ')
        if (input1.split(".")[-1] == "txt" and os.path.exists(input1)):
            f = input1
            break
        else:
            print ("File type not supported or file doesn't exist")

    print ("Starting ...")
    print ("")
    emails_found = False
    for email in find_emails(open(f).read().lower()):
        print ("Email Found: " + email)
        emails_found = True

    if (not emails_found):
        print ("No Emails found")
