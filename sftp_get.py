#!/usr/bin/env python
#coding=UTF-8
import paramiko
import sys,os
print "####################从服务器下载文件###################"
print "-------远程路径：/hskj/tmp/bjywb/getdate/,本地路径：/tmp/-------"
host = raw_input("请输入IP地址：")
port = int(raw_input("请输入端口："))
username = 'bjywb'
name = raw_input("请输入文件名：")
rfilename = "/hskj/tmp/bjywb/getdate/"+name
lfilename = "/tmp/"+name

pkey_file='/home/ywget1/.ssh/hskj_20130620_bjywb'
t = paramiko.Transport((host,port))
key = paramiko.RSAKey.from_private_key_file(pkey_file,'&U*I(O1208')
t.connect(username=username,pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get(rfilename,lfilename)
t.close()
