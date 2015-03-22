from sys import argv
import os.path
import os
import paramiko
import random
import sqlite3

options = ["download", "upload"]
script, action, filename = argv
print "Uploading filename: %s" % filename

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
            print "Your file has been successfully uploaded to our servers."
            print "The ID of the file for download is: %i" % fileID
            print "The file will be removed in 24 hours."
        except IOError, e:
            print e
            print "Oh no! An error has occured when uploading the file to our servers."
    else:
        print "File you are trying to upload does not exist."

def download(filename):
    try 
    filepath = '/home/%s' % filename
    localpath = os.getcwd() + '/%s' % filename
    sftp.get(filepath, localpath)

if action.lower() in options:
    if action.lower() == "upload":
        upload(filename)
    elif action.lower() == "download":
        download(filename)
else:
    print "no"
