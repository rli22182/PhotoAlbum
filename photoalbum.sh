#!/bin/bash
#
# Author: Rui Li
#
#This runs the photoalbum service in the background. Support start|stop|restart.

service='photoalbum-0.0.1-SNAPSHOT'


kill_process(){
process=$1
suffix=".pid"
PIDFile=$process$suffix
if [ -e "$PIDFile" ]; then
  PID=`cat $PIDFile`
  CHKPID=`ps -p $PID`
  if [ -n "$CHKPID" ]; then
    kill -9 $PID
    echo "[`date '+%Y-%m-%d %H:%M:%S'`][INFO] $service is stopped." >> ${LOG} 2>&1
  else
    rm -f $PIDFile
  fi
fi
}

START=$(date +%s)

END=$(date +%s)
DIFF=$(( $END - $START ))

MPATH=`dirname $0`
CURR=`pwd`
cd "$MPATH"
MPATH=`pwd`

if [ $# != 1 ]; then
  echo "Usage: photoalbum.sh start|stop|restart"
elif [ $1 == "stop" ]; then
  echo "Stopping..."
  mkdir -p $MPATH/logs
  LOG=$MPATH/logs/photoalbum_`date +%Y-%m-%d`.log
  kill_process $service >>${LOG} 2>&1
  sleep 5
  echo "[`date '+%Y-%m-%d %H:%M:%S'`][INFO] Done! Please check log file: ${LOG} for details."
elif [ $1 == "restart" ] || [ $1 == "start" ]; then
  if [ $1 == "restart" ]; then
  	echo "Stopping..."
  fi
  mkdir -p $MPATH/logs
  LOG=$MPATH/logs/photoalbum_`date +%Y-%m-%d`.log
  kill_process $service >>${LOG} 2>&1
  echo "Starting..."
  nohup java -jar /target/${service}.jar >> $LOG 2>&1 < /dev/null &
  echo $! > ${service}.pid
  echo "[`date '+%Y-%m-%d %H:%M:%S'`][INFO] Done! Please check log file: ${LOG} for details."
else
  echo "Usage: photoalbum.sh start|stop|restart"
fi

cd "$CURR"
exit