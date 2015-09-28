#!/usr/bin/env python
import paramiko
import sys,os
host = '210.14.134.80'
port = 22
username = 'bjxtb'
pkey_file='/home/bjxtb/.ssh/id_rsa'
s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file(pkey_file)
s.connect(host,port,username,pkey=key,timeout=10)
cmd = 'grep -a "13261289750" /hskj/logs/gate/receiver.txt | head -3'
stdin,stdout,stderr = s.exec_command(cmd)
#cmd_result = stdout.readlines(),stderr.readlines()
#print (cmd_result)
#print (host)
table_list = []
for result in stdout.readlines():
    table_list.append({'content':result.strip("\n")})
print (table_list)
s.close()
