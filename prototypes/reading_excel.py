import pandas as pd


filename = "/Users/zebedeemarsh/Documents/Coding/CS Project main/CS-Project/output1.xls"
df = pd.read_excel(filename)
print(df)

timearray = df['Time']
# print(timearray)
ls = df.values.tolist()
# print(ls)
