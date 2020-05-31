#!/bin/bash
max=$1
for i in `seq 2 $max`
do
    curl -w "@curl-format.txt" -o /dev/null -s $2 | tee -a $3
done 
