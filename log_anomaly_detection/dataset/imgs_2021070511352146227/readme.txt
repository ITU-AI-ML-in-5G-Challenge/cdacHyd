Data Description

Train dataset:
1、messages_trainset.txt，time frame is from 20210311 to 20210430, without anomalies
2、sysmonitor_trainset.txt, time frame is from 20210301 to 20210420, without anomalies

Test dataset:
1、messages_testset.txt，time frame is from 20210501 to 20210511, with some anomalies, such as server power down, insufficient memory
2、sysmonitor_testset.txt, time frame is from 20210421 to 20210501, with some anomalies, such as server power down


result_format.csv, participants should add a Label column in this file, 0 for no anomalies and 1 for anomalies, for example:

LogName,TimeSlice,Label
messages,5399328,0
messages,5399329,0
messages,5399330,0
messages,5399331,1
messages,5399332,1
messages,5399333,0
messages,5399334,0
messages,5399335,0

Note: The TimeSlice column in result_format.csv is generated according to the time in the test dataset. The time in the test dataset is converted into a timestamp, then divided by 300 and rounded as the value of TimeSlice, which means 5 minutes as a time slice.

*******************************
abnormal kewords:
down
powers
abnormal
