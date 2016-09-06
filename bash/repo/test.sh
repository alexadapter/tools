#!/bin/bash

#if[[ $1 == "name="]]

var=$1
cat $var | while read p; do 
#echo $p;
tmp=${p##*name=\"}
#echo $tmp

tmp1=${tmp%%\"*}
echo $tmp1
done;






