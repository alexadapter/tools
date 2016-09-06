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
#	echo $namet 
#	echo $namet $path
	echo $path
else
	
tmp1=${p##*name=\"}

	if [[ "$tmp1" != "<"* ]];
		then
		tmp2=${tmp1%%\"*}
	#	echo $tmp2 
		#echo $tmp2 $tmp2
		echo $tmp2
	fi
fi
#tmp1=${tmp%%\"*}
#echo $tmp1
done;
