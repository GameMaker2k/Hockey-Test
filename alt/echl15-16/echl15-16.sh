#!/usr/bin/env bash
leaguename="echl"
year="15-16"
getcwd="`pwd`"
rm -rfv "${getcwd}/${leaguename}${year}.log"
time python "${getcwd}/${leaguename}${year}.py" "../hockey15-16.db3" 2>&1 | tee -a "${getcwd}/${leaguename}${year}.log"
sync
