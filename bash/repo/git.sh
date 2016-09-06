#!/bin/bash
var=$1
cat $var |while read p; 

do 
tmp=${p##* }
tmp1=${p%% *}
#echo $tmp
#echo $tmp1

cd $tmp
git init .
git add .
git commit -m "bak from QComm"
git remote add C8 android-repo@git.dream:repo/QComm/C8/$tmp1.git

done






