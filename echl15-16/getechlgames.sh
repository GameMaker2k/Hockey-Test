#!/bin/bash
leaguename="echl"
i="9"
echo "Games From ${leaguename}"
echo ""
while [ $i -lt 10 ]; do
sleep 10s
python "./get${leaguename}games.py" "$i" "10" "2015"
echo ""
i=$[$i+1]
done;
