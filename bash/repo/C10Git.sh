#!/bin/bash

var=$1
var2=$2
i=0

cat $var |while read p; 
do

tmp=$p
j=0

cat $var2 | while read p1;
do 

if [ $j -eq $i ]; then

tmp1=$p1

echo $tmp $tmp1
# git init 
# git add --all .
# git commit -m "first commit"
# git remote 
break;

else
let "j=j+1"
continue;
fi
done

let "i=i+1"

done

