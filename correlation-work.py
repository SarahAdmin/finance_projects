import pandas as pd
finDF = pd.read_excel('NCCG 2324 accounts workings data.xlsx',sheet_name='Check of bank statement')
columns_to_delete = ['Period','Period.1', 'Cash opening.1', 'Receipts.1',
       'Payments.1', 'Bank Cash closing.1', 'Check.1', 'Difference.1']
finance_data = finDF.drop(columns_to_delete,axis=1)
fin_correlations = finance_data.corr(method='pearson')
print(fin_correlations.to_string())
