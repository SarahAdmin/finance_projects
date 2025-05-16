import pandas as pd 
finDF = pd.read_excel('NCCG 2324 accounts workings data.xlsx',sheet_name='Check of bank statement')
duplicatedFinance = finDF.duplicated()
print(duplicatedFinance)
