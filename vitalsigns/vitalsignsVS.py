import pandas as pd
pul = pd.read_csv("pulse.csv")
# Select the pulse_rate and cattle_gender columns from the DataFrame
x  = pul[['pulse_rate', 'cattle_gender']]

calves = []
adults = []
abnormal =[]
for  index, row in pul.iterrows():
     pulse_rate = float(row['pulse_rate'])
     if pulse_rate>=100 and pulse_rate<=150:
         calves.append({'cattle_id':row['cattle_id'], 'pulse_rate':row['pulse_rate']})
     elif pulse_rate >= 45 and pulse_rate <= 85:
         adults.append({'cattle_id':row['cattle_id'], 'pulse_rate':row['pulse_rate']})
     else:
         abnormal.append({'cattle_id':row['cattle_id'],'pulse_rate':row['pulse_rate']})
#print(calves)
# print(adults)
# print("abnornal ",abnormal)
for i in abnormal:
    print(" Cattle with id {0} has an abnormal pulse rate of {1}".format(i['cattle_id'],i['pulse_rate']))
