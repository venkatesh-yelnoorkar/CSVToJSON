import csv
import json
import copy

#set the default url
url = "abc.com/"
#open all the csv files.
file1 = "file1.csv"
file2 = 'file2.csv'

with open(file1) as f1:
    with open(file2) as f2:
        csv1 = csv.reader(f1, delimiter = ',')
        csv2 = csv.reader(f2, delimiter = ',')

        #print(type(csv1))
        #print(type(csv2))

        #extract the columns of component and project id
        components = []
        projectids = []
        for row in csv2:
            component = row[0]
            projectid = row[1]

            components.append(component)
            projectids.append(projectid)
        #print(projectids)
        #print(len(projectids))

        #create the temp dict and final list of dicts
        ldicts = []
        temp = {}
        #find project id for every row in csv1
        for row in csv1:
            #print(row[4])

            try:
                ind = components.index(row[4])
                print(row[4], ind)
                #error if instance is not associated with any project
            except Exception as e:
                #if no project is associated the PROJECTID = -2
                print(e)
                temp['ProjectID'] = '-2'
            else:
                #get the numeric proid
                proid = projectids[ind].split(sep = '-')[0]
                print(proid)

                if(proid.isnumeric()):
                    temp['ProjectID'] = proid
                else:
                    #ProjectID=-1 if invalid proid
                    temp['ProjectID'] = '-1'

            finally:
                temp["Component"] = row[4]
                temp["URL"] = url+row[4]

                print(temp)
                t = copy.deepcopy(temp)
                #add the temp to ldicts
                ldicts.append(t)
                print(len(ldicts))
                print(ldicts)


        #make json out of the ldicts

        with open('data.json', 'w') as json_file:
            json.dump(ldicts, json_file)
