#!/bin/bash
year="15-16"
getcwd="`pwd`"
rm -rfv "${getcwd}/hockey${year}-games.log"
cd "./echl${year}/"
getcwd="`pwd`"
time bash "${getcwd}/getechlgames.sh" 2>&1 | tee -a "${getcwd}/../hockey${year}-games.log"
sync
cd "./../"
cd "./ahl${year}/"
getcwd="`pwd`"
time bash "${getcwd}/getahlgames.sh" 2>&1 | tee -a "${getcwd}/../hockey${year}-games.log"
sync
cd "./../"
cd "./nhl${year}/"
getcwd="`pwd`"
time bash "${getcwd}/getnhlgames.sh" 2>&1 | tee -a "${getcwd}/../hockey${year}-games.log"
sync
cd "./../"
getcwd="`pwd`"
