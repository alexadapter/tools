#!/bin/bash

#if[[ $1 == "name="]]

var=$1
cat $var | while read p; do 
#echo $p;
tmp=${p##*path=\"}
#echo $tmp

if [[ "$tmp" != "<"* ]];
then
#echo $tmp
path=${tmp%%\"*}

name=${p##*name=\"}
namet=${name%%\"*}
	#statements

	echo $namet $path
fi
#tmp1=${tmp%%\"*}
#echo $tmp1
done;
