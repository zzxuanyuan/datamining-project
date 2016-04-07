#!/bin/sh

DATAPATH=$(pwd)/../data
for csvdata in $DATAPATH/*.csv; do
	echo "name:$csvdata"
	dataname=data.${csvdata#$DATAPATH/}
	python preprocess.py $csvdata 32 $dataname
done

if [ -e activity.tempdata.csv ]
then
	rm activity.tempdata.csv
fi

cat data.*.csv >> activity.tempdata.csv

if [ -e activity.data.csv ]
then
	rm activity.data.csv
fi

echo "$(head -1 activity.tempdata.csv)" >> activity.data.csv
while read LINE
do

	if [[ "$LINE" != *"DC"* ]]; then
		echo "$LINE" >> activity.data.csv
	fi
done < activity.tempdata.csv

rm *.tempdata.csv

TESTPATH=$(pwd)/../test
for csvtest in $TESTPATH/*.csv; do
	echo "name:$csvtest"
	testname=test.${csvtest#$TESTPATH/}
	python preprocess.py $csvtest 32 $testname
done

if [ -e activity.temptest.csv ]
then
	rm activity.temptest.csv
fi

cat test.*.csv >> activity.temptest.csv

if [ -e activity.test.csv ]
then
	rm activity.test.csv
fi

echo "$(head -1 activity.temptest.csv)" >> activity.test.csv
while read LINE
do

	if [[ "$LINE" != *"DC"* ]]; then
		echo "$LINE" >> activity.test.csv
	fi
done < activity.temptest.csv


rm *.temptest.csv
rm data.*.csv
rm test.*.csv
