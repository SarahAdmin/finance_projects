import pandas as pd
finDF = pd.read_excel('NCCG 2324 accounts workings data.xlsx',sheet_name='Check of bank statement')
columns_to_delete = ['Period.1', 'Cash opening.1', 'Receipts.1',
       'Payments.1', 'Bank Cash closing.1', 'Check.1', 'Difference.1']
new_finance = finDF.drop(columns_to_delete, axis=1)
total_cash_opening = new_finance['Cash opening'].sum()
total_receipts = new_finance['Receipts'].sum()
total_payments = new_finance['Payments'].sum()
total_cash_closing = new_finance['Bank Cash closing'].sum()
total_check = new_finance['Check'].sum()
print(new_finance.to_string())
print(f'The total cash opening: {total_cash_opening}.')
print(f'The total receipts: {total_receipts}.')
print(f'The total payments: {total_payments}.')
print(f'The total cash closing: {total_cash_closing}.')
print(f'The total check: {total_check}')
