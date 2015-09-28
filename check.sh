#!/bin/bash

value=`find /hskj/script/log -mtime -1 -name "chpasswd.log" |wc -l`

if [ $value -gt 0 ];then
echo yunwei:yunwei336688 |chpasswd
curl --data "account=yunwei&passwd=123&emailwarning=1&email=jinyalin@hongshutech.com&smswarning=1&mobile=13261289750&content=被修改的系统账号密码已经改回原来的，知悉" http://yj.baiwutong.com:8180/PlateWarning
fi
