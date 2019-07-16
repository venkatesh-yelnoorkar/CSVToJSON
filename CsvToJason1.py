import csv
import json

url = "https://rtc.nam.nsroot.net/cto"

#create empty list of dicts
ldicts  = []
temp = {}
seperator = ""

#open the files
file = "file2.csv"
print(1)
with open(file) as f:
    csvr = csv.reader(f, delimiter = ",")

    #create dict and append to ldicts
    for row in csvr:
        temp["Instance name"] = row[0]
        temp["Instance URL"] = url + row[0]
        print(2)
        l = []
        for t in row[1]:
            print(3)
            print(t)
            if t.isdigit():
                l.append(t)
                print(4)
            else:
                break

        if len(l)>0:
            proid = seperator.join(l)
            temp["Collection"] = str(proid)
            t = copy.deepcopy(temp)
            #add the temp to ldicts
            ldicts.append(t)
            print(len(ldicts))
