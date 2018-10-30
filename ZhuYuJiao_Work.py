import pandas as pd


file_path = r'D:\CodeProject\FirstTemplate\联想TN.xls'
Dataframe = pd.read_excel(file_path, header=0, index_col=0)
target_col = pd.DataFrame(Dataframe['联想_TN'], dtype=str)


def string_cLean(string):
    if not string:
        return None
    for i in range(len(string)):
        if string[:i] and string[:i] == string[i:2*i]:
            return string_cLean(string[i:])
    return string


target_col['联想_TN'] = target_col['联想_TN'].apply(string_cLean)
target_col.to_excel('联想_TN_2.xls')
