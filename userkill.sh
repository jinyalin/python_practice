#!/bin/bash
PIDALL=`ps -ef |grep ssh |grep -v "ps" |awk '{print $2}'`
for i in ${PIDALL}
 do
  kill -9 ${i}
 done
