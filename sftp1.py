#/usr/bin/env python
import os,sys
import paramiko
import threading
class worker(threading.Thread):
    def __init__(self,server=None,username=None,port=None,command=None,pkey_file=None):
        threading.Thread.__init__(self)
        self.server=server
        self.username=username
        self.port=port
        self.command=command
        self.pkey_file=pkey_file
        self.thread_stop=False
    def run(self):
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        key = paramiko.RSAKey.from_private_key_file(self.pkey_file)
        s.connect(self.server,self.port,self.username,pkey=key,timeout=10)
        stdin,stdout,stderr = s.exec_command(self.command)
        table_list = []
        for result in stdout.readlines():
            table_list.append({'server':self.server,'content':result})
        print(table_list)
        s.close()
    def stop(self):
        self.thread_stop=True

                
if __name__=="__main__":
        command = "ls /tmp"
        username = 'bjxtb'
        pkey_file='/home/bjxtb/.ssh/id_rsa'
        server = "211.103.155.220"
        port = 22
        table_list = []
        cmd_thread=worker(server,username,port,command,pkey_file)
        cmd_thread.start()
        cmd_thread.stop()
