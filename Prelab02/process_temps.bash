#! /bin/bash
#
#$Author: ee364a07 $
#$Date: 2016-09-04 22:21:38 -0400 (Sun, 04 Sep 2016) $
#$Revision: 93049 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab02/process_temps.bash $
#$Id: process_temps.bash 93049 2016-09-05 02:21:38Z ee364a07 $

if (( $# != 1 ))
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
else
    count=1
    while read line; do
        if (( $count >=2 ))
        then
            IFS='       ' read -r -a array <<< $line
            time=${array[0]}
            unset array[0]
            array=("${array[@]}")
            num=${#array[*]}
            sum=0
            for item in ${array[*]}
            do
                ((sum=$sum+$item))
            done
            ((average=$sum/$num))
            echo "Average temperature for time $time was $average C."
        fi
        ((count=$count+1))
    done < $1
fi
exit 0
