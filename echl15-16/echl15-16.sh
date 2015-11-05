#!/usr/bin/env bash
leaguename="echl"
year="15-16"
getcwd="`pwd`"
rm -rfv "${getcwd}/${leaguename}${year}.log"
time python "${getcwd}/${leaguename}${year}.py" 2>&1 | tee -a "${getcwd}/${leaguename}${year}.log"
sync
