#/opt/local/bin/python3.4

from sys import argv
import os.path
import os
import paramiko
import random
import sqlite3
import shutil
paramiko.util.log_to_file('paramiko.log')


options = ["download", "upload"]
script, action, filename = argv

fileID = random.randrange(1000,10000) # >> change to dict

host = "107.170.160.225"
port = 22
transport = paramiko.Transport((host, port))

password = "updl1234"
username = "root"
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)    

def upload(filename):
    if os.path.isfile(filename):
        try:
            filepath = '/home/%s' % filename
            localpath = os.getcwd() + '/%s' % filename
            sftp.put(localpath, filepath)
        except IOError:
            print("Oh no! An error has occured when uploading the file to our servers.")
    else:
        print("File you are trying to upload does not exist.")

def download(filename):
    filepath = '/home/%s' % filename
    localpath = os.getcwd() + '/%s' % filename
    sftp.get(filepath, localpath)

if __name__ == "__main__":
    if action.lower() in options:
        if action.lower() == "upload":
            if filename.endswith((".txt", ".png", ".zip")) == False:
                print("Converting directory to zip...")
                shutil.make_archive(filename, "zip", filename)
                print("Success! Uploading...")
                upload(filename+".zip")
                print("Success! Removing zip from your computer...")
                os.remove(filename+".zip")
                print("Success! Your directory has been uploaded.")
            else:
                print("Uploading file...")
                upload(filename)
                print("Success! Your ID is 1234.")
        elif action.lower() == "download":
            if filename.endswith((".txt", ".png")) == False:
                print("Downloading directory...")
                download(filename+".zip")
                print("Converting from zip to directory...")
                shutil.unpack_archive(filename+".zip", filename)
                print("Removing the zip file from your computer...")
                os.remove(filename+".zip")
                print("Success! The directory has been downloaded.")
            else:
                print("Downloading file...")
                download(filename)
                print("Success! Your file has been downloaded.")
    else:
        print("no")
