#!/usr/bin/env python
#coding=UTF-8
import paramiko
import sys,os
host = raw_input("请输入IP地址：")
#host = '210.14.134.79'
#host = '103.26.1.137'
#host = '183.192.160.22'
port = int(raw_input("请输入端口："))
#port = 22
username = 'bjywb'
name = raw_input("请输入文件名：")
lfilename = "/tmp/"+name
rfilename = "/tmp/"+name
#lfilename = "/tmp/yw.sh"
#rfilename = "/tmp/yw.sh"

pkey_file='/home/ywget1/.ssh/hskj_20130620_bjywb'
t = paramiko.Transport((host,port))
key = paramiko.RSAKey.from_private_key_file(pkey_file,'&U*I(O1208')
t.connect(username=username,pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(lfilename,rfilename)
t.close()
