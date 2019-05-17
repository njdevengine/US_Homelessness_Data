import requests
url = "https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-State.xlsx"
resp = requests.get(url)

filename = 'data.xlsx'

output = open(filename, 'wb')
output.write(resp.content)
output.close()

import pandas as pd
data = []

for i in range(0,13):
    df = pd.read_excel(filename,sheet_name=i)
    data.append(df)
    
df = data[0][["state"]]

#gets the second column from 2018 data on homeless totals
n = 2018
for i in range(1,len(data)):
    df[str(n)] = (list(data[i].iloc[:,2]))
    n-=1
