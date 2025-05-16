import pandas as pd
finDF = pd.read_excel('NCCG 2324 accounts workings data.xlsx',sheet_name='Check of bank statement')
columns_to_delete = ['Period.1', 'Cash opening.1', 'Receipts.1',
       'Payments.1', 'Bank Cash closing.1', 'Check.1', 'Difference.1']
new_finance = finDF.drop(columns_to_delete, axis=1) 
average_cash_opening = new_finance['Cash opening'].mean()
average_receipts = new_finance['Receipts'].mean()
average_payments = new_finance['Payments'].mean()
average_cash_closing = new_finance['Bank Cash closing'].mean()
average_check = new_finance['Check'].mean()
print(new_finance.to_string())
print(f'The average cash opening: {average_cash_opening}.')
print(f'The average receipts: {average_receipts}.')
print(f'The average payments: {average_payments}.')
print(f'The average cash closing: {average_cash_closing}.')
print(f'The average check: {average_check}')
