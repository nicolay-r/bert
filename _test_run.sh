#!/bin/bash

for i in $m1; do

    OLDIFS=$IFS
    IFS=','

    # Split into
    # $1 -- folder,
    # $2 -- task_name
    set -- $i;

    folder=$1
    task_name=$2

    src=./data/$1

    ./run_classifier.sh 0 $folder $task_name

done;

IFS=$OLDIFS