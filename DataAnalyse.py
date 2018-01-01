import pandas as pd
from pandas import DataFrame
filepath = r"C:\Users\Silver\\Desktop\\dataattamp.xlsx"
df = pd.read_excel(filepath,skiprows=[0],index_col=0)
new_list = []
element = []
for each in df.values:
	for every in each:
		new_value = str(every)
		element.append(new_value)# 提取第一位时new_value[3]，如果要提取后面的就依次增加
	new_list.append(element)
	element = []
	new_index = []
for each in df.index:
	value = str(each)[-4:-1]
	new_index.append(value)
new_df = DataFrame(new_list,columns = ['000','001','011','010'],index= new_index)
print(new_df)



