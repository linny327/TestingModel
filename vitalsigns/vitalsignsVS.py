import pandas as pd
import numpy as  np

pul = pd.read_csv("pulse.csv")
#print(pul.head)
#print(pul.pulse_rate)
# Select the pulse_rate and cattle_gender columns from the DataFrame
x  = pul[['pulse_rate', 'cattle_gender']]
print(x)
# iterating the columns
for col in pul.columns:
    print(col)
#listing columns
list(pul.columns)
print("*************")
for( columnName, columnData) in pul.iteritems():
    print('column contents : ', columnData.values)
    y = columnData.values
    if(45<y<85):
        print("pulse or heart rate is abnormal")
