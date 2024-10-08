#!/bin/bash
leaguename="ahl"
i="30"
echo "Games From ${leaguename}"
echo ""
while [ $i -lt 32 ]; do
sleep 10s
python "./get${leaguename}games.py" "$i" "01" "2016"
echo ""
i=$[$i+1]
done;
