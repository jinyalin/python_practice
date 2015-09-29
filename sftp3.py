#!/usr/bin/env python
import paramiko
import sys,os
host = '210.14.134.77'
#host = '103.26.1.137'
#host = '183.192.160.22'
port = 10074
#port = 22
username = 'bjxtb'
lfilename = "/tmp/setUserSplitFlowTd.jsp"
rfilename = "/hskj/tomcat_manager_new/webapps/financeSystem/WEB-INF/page/userManage/userServiceInfo/setUserSplitFlowTd.jsp"
#lfilename = "/tmp/yw.sh"
#rfilename = "/tmp/yw.sh"

pkey_file='/home/bjxtb/.ssh/id_rsa'
t = paramiko.Transport((host,port))
key = paramiko.RSAKey.from_private_key_file(pkey_file)
t.connect(username=username,pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(lfilename,rfilename)
t.close()
remote_cmd = "ssh "+username+"@"+host+" -p "+str(port)+" md5sum "+rfilename+"| awk '{print $1}'"
#print("remote_cmd:"+remote_cmd)
local_cmd = "md5sum "+lfilename +"| awk '{print $1}'"
remote_md5 = os.popen(remote_cmd)
rmd5 = remote_md5.read().strip()
print("rmd5:"+rmd5)
local_md5 = os.popen(local_cmd)
lmd5 = local_md5.read().strip()
print("lmd5:"+lmd5)
if lmd5 == rmd5:
    print("上传成功，校验一致~")
else:
    print("校验不一致！请检查")
