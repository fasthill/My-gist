# write-dictionary.py

import csv

ndict=[{'name':'Andrew','rollno.':1,'marks':19},
       {'name':'John','rollno.':2,'marks':18},
       {'name':'Roger','rollno.':3,'marks':16}]
#define fields
fields=['rollno.','name','marks'] # == fileds=ndict[0].keys()

with open('dictnew.csv',mode='w') as file:
    writer=csv.DictWriter(file,fieldnames=fields)#create writer object
    writer.writeheader() #writing field names(headings)
    writer.writerows(ndict) #writing the data
    
#---------List-----------------------------
#defining fields
fields=['Rollno.','Name','Marks']

#defining data
data= [[1,'Andrew',20],
       [2,'Roger',18],
       [3,'John',14],
       [4,'Dipin',17]]

#opening a new csv file
with open('file.csv',mode='w') as file:
    writer=csv.writer(file) #defing csv writer object
    writer.writerow(fields) #writing the fields
    writer.writerows(data)   #writing the data
    
#---------List-----------------------------
f = open('file2.csv',mode='w')
writer=csv.DictWriter(f,nn.keys())
writer.writeheader()
writer.writerow(nn)
f.close()

