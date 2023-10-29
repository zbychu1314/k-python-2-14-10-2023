import csv
import pandas as pd
df = pd.read_csv('file3.csv',encoding='utf-8',delimiter=',',on_bad_lines='skip')
print(df)   
#    print(csv_reader)
    #for row in csv_reader:
     #   print(row)
    #print(csv_reader)

