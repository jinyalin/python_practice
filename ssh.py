#!/usr/bin/python
#coding=UTF-8
import os,sys
import pexpect
import struct
import fcntl
import termios
import signal
reload(sys)
sys.setdefaultencoding('utf8')
def sigwinch_passthrough (sig, data):
    winsize = getwinsize()
    global ssh
    ssh.setwinsize(winsize[0],winsize[1])
def getwinsize():
    if 'TIOCGWINSZ' in dir(termios):
        TIOCGWINSZ = termios.TIOCGWINSZ
    else:
        TIOCGWINSZ = 1074295912L # Assume
    s = struct.pack('HHHH', 0, 0, 0, 0)
    x = fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ, s)
    return struct.unpack('HHHH', x)[0:2]

def mainMethod(group,flag,keydir,user):
    ip_file = '/hskj/script/ip.txt'
    ip_dic = {}
    num = 0
    f = file(ip_file)
    for line in f.readlines():
        f.close()
        if flag==1:
            print line,
            if '------' in line:continue
            if line.count('\n')==len(line):continue
            f_line = line.strip().split()
            num = f_line[0]
            host = f_line[2]
            port = f_line[5]
            if len(line) == 0:break
            ip_dic[num] = 'ssh -o ServerAliveInterval=60 -o StrictHostKeyChecking=no -i '+keydir+'/.ssh/hskj_20130606_'+user+' '+user+'@%s -p %s'  %(host,port)
        else:
            if flag==2:
                userGroups = group.strip().split(",")
                for userGgroup in userGroups:
                    if userGgroup == "短信组":
                        if userGgroup in line or '---' in line or '    ' in line:
                            print line,  
                            if '------' in line:continue
                            if line.count('\n')==len(line):continue
                            f_line = line.strip().split()
                            num = f_line[0]
                            host = f_line[2]
                            port = f_line[5]
                            if len(line) == 0:break
                            ip_dic[num] = 'ssh -o ServerAliveInterval=60 -o StrictHostKeyChecking=no -i '+keydir+'/.ssh/hskj_20130606_'+user+' '+user+'@%s -p %s'  %(host,port)
                    else:
                        if userGgroup in line:
                            print line,  
                            if '------' in line:continue
                            if line.count('\n')==len(line):continue
                            f_line = line.strip().split()
                            num = f_line[0]
                            host = f_line[2]
                            port = f_line[5]
                            if len(line) == 0:break
                            ip_dic[num] = 'ssh -o ServerAliveInterval=60 -o StrictHostKeyChecking=no -i '+keydir+'/.ssh/hskj_20130606_'+user+' '+user+'@%s -p %s'  %(host,port)
    if flag==0:
        print "您没有权限查看任何服务器~请联系管理员~"
    else:
        try:
            option = raw_input("请选择:\n")
            if option in ip_dic.keys():
                ssh = pexpect.spawn(ip_dic[option])
                ssh.expect("key")
                ssh.sendline("&U*I(O1208")
                ssh.expect("$")
                ssh.sendline("echo name "+name)
                signal.signal(signal.SIGWINCH, sigwinch_passthrough)
                size = getwinsize()
                ssh.setwinsize(size[0], size[1])
                ssh.interact()
            else:
                print "您输入的服务器标识不存在！"
        except (Exception,SyntaxError,KeyboardInterrupt):
            print "您输入的内容存在问题，请重新输入!"
if __name__=="__main__":
        lname = os.popen("id -un")
        name = lname.read().strip()
        keydir = "/home/"+name
        flag = ""
        group = ""
        user = "bjyfb"
        fu = file("/hskj/script/UserGroup.txt")
        for line in fu.readlines():
            gline=line.strip().split()
            if gline[0]==name:
                if gline[1]=='运维组':
                    flag=1
                    user="bjywb"
                    mainMethod(group,flag,keydir,user)
                else:
                    if gline[1]=='系统组':
                        flag=1
                        user="bjxtb"
                        mainMethod(group,flag,keydir,user)
                    else:
                        if gline[1]=='root':
                            flag=1
                            user="root"
                            keydir="/root"
                            mainMethod(group,flag,keydir,user)
                        else:
                            if gline[1]=='BI组' or gline[1]=='主管':
                              flag=1
                              user="bjyfb"
                              while True: 
                                  mainMethod(group,flag,keydir,user) 
                            else:
                                group=gline[1]
                                flag=2
                                while True: 
                                  mainMethod(group,flag,keydir,user)

