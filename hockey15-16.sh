#!/usr/bin/env bash

year="15-16"
getcwd="`pwd`"
rm -rfv "${getcwd}/hockey${year}.log"
rm -rfv "${getcwd}/hockey${year}.db3"
rm -rfv "${getcwd}/hockey${year}.tar.xz"
rm -rfv "${getcwd}/hockey${year}-games.log"
cd "./echl${year}/"
getcwd="`pwd`"
time bash "${getcwd}/echl${year}.sh" 2>&1 | tee -a "${getcwd}/../hockey${year}.log"
sync
cd "./../"
cd "./ahl${year}/"
getcwd="`pwd`"
time bash "${getcwd}/ahl${year}.sh" 2>&1 | tee -a "${getcwd}/../hockey${year}.log"
sync
cd "./../"
cd "./nhl${year}/"
getcwd="`pwd`"
time bash "${getcwd}/nhl${year}.sh" 2>&1 | tee -a "${getcwd}/../hockey${year}.log"
sync
cd "./../"
getcwd="`pwd`"
time tar -cvf "./hockey${year}.tar" --exclude="*.tar" "."
xz -z -9 -e -v "${getcwd}/hockey${year}.tar"
sync

