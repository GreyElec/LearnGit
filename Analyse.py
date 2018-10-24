import pandas as pd
import numpy as np
from pandas import DataFrame


filepath = r"C:\Users\Silver\Desktop\globalterrorismdb_0617dist.csv"
f_data = pd.read_csv(filepath,encoding='ISO-8859-1')
NewData = DataFrame(f_data)
NewData.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)
NewData= NewData[['Year','Month','Day','Country','Region','city','latitude','longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]
print(NewData.head(3))
print("**************************")
print(NewData.isnull().sum())
print("**************************")
print("Country with the highest Terriost Attacks:",NewData["Country"].value_counts().index[0:3],NewData["Country"].value_counts()[0:3])
print(NewData["AttackType"].value_counts()[0:10])