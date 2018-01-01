import pandas as pd
from pandas import DataFrame

filepath = r"C:\Users\Silver\Desktop\syndata.xlsx"

df = pd.read_excel(filepath,index_col=0)
def data(f):
	element = []
	for each in df.values:
		for every in each:
			new_element = str(every)
			element.append(new_element[-1])
	return element
new_data = data(df)
#print(df)
new_data = DataFrame(new_data,index = df.index)
print(new_data)