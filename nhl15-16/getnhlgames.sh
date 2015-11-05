#!/bin/bash
leaguename="nhl"
i="7"
echo "Games From ${leaguename}"
echo ""
while [ $i -lt 8 ]; do
sleep 10s
python "./get${leaguename}games.py" "$i" "10" "2015" "2016"
echo ""
i=$[$i+1]
done;
