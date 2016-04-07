#!/bin/sh

if [ -e activity.*.csv ]
then
	rm activity.*.csv
fi

CURPATH=$(pwd)
python preprocess.py $CURPATH/../data/run1.csv 32 run1.feature.csv
python preprocess.py $CURPATH/../data/run2.csv 32 run2.feature.csv
python preprocess.py $CURPATH/../data/run3.csv 32 run3.feature.csv
python preprocess.py $CURPATH/../data/run4.csv 32 run4.feature.csv
python preprocess.py $CURPATH/../data/sit1.csv 32 sit1.feature.csv
python preprocess.py $CURPATH/../data/sit2.csv 32 sit2.feature.csv
python preprocess.py $CURPATH/../data/sit3.csv 32 sit3.feature.csv
python preprocess.py $CURPATH/../data/sit4.csv 32 sit4.feature.csv
python preprocess.py $CURPATH/../data/stand1.csv 32 stand1.feature.csv
python preprocess.py $CURPATH/../data/stand2.csv 32 stand2.feature.csv
python preprocess.py $CURPATH/../data/stand3.csv 32 stand3.feature.csv
python preprocess.py $CURPATH/../data/stand4.csv 32 stand4.feature.csv
python preprocess.py $CURPATH/../data/upstairs1.csv 32 upstairs1.feature.csv
python preprocess.py $CURPATH/../data/upstairs2.csv 32 upstairs2.feature.csv
python preprocess.py $CURPATH/../data/upstairs3.csv 32 upstairs3.feature.csv
python preprocess.py $CURPATH/../data/upstairs4.csv 32 upstairs4.feature.csv
python preprocess.py $CURPATH/../data/downstairs1.csv 32 downstairs1.feature.csv
python preprocess.py $CURPATH/../data/downstairs2.csv 32 downstairs2.feature.csv
python preprocess.py $CURPATH/../data/downstairs3.csv 32 downstairs3.feature.csv
python preprocess.py $CURPATH/../data/downstairs4.csv 32 downstairs4.feature.csv

if [ -e activity.tempdata.csv ]
then
	rm activity.tempdata.csv
fi

cat *1.feature.csv >> activity.tempdata.csv
cat *2.feature.csv >> activity.tempdata.csv
cat *3.feature.csv >> activity.tempdata.csv
cat *4.feature.csv >> activity.tempdata.csv

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

python preprocess.py $CURPATH/../data/run5.csv 32 run5.feature.csv
python preprocess.py $CURPATH/../data/sit5.csv 32 sit5.feature.csv
python preprocess.py $CURPATH/../data/stand5.csv 32 stand5.feature.csv
python preprocess.py $CURPATH/../data/upstairs5.csv 32 upstairs5.feature.csv
python preprocess.py $CURPATH/../data/downstairs5.csv 32 downstairs5.feature.csv

if [ -e activity.temptest.csv ]
then
	rm activity.temptest.csv
fi

cat *5.feature.csv >> activity.temptest.csv

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
rm *.feature.csv
