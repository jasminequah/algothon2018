from datetime import datetime

dt1 = datetime(2018, 1, 2, 0, 0)
dt2 = datetime(2018, 7, 31, 23, 0)

dic = {str(dt1): str(2.100764), str(dt2): str(2.101739)} #test result

download_dir = "result.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "time stamp, mid-price\n"
csv.write(columnTitleRow)

for key in dic.keys():
	timestamp = key
	midprice = dic[key]
	row = timestamp + ", " + midprice + "\n"
	csv.write(row)