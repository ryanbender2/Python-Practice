"""
    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
    VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
"""

import pandas as pd

def insert(table, columns, values, qry_name):
    sql_file_exists = True
    
    try:
        t = open(qry_name)
    except FileNotFoundError:
        sql_file_exists = False
    print(str(values))
    insert_line = "INSERT INTO {0} ({1})\n".format(table, ', '.join(columns))


table = 'BillingRates'
# cols = ['EmployeeTypeID', 'SkillLevelID', 'BillingRate']

# values = [[1.0, 2.0, 160.0], [1.0, 3.0, 175.0], [2.0, 1.0, 135.0], [2.0, 2.0, 140.0]]
df = pd.read_csv('Billing_Rates.csv', dtype=str)
values = [[i.strip() for i in row] for row in df.values]
cols = [i.strip() for i in df.columns]
dtype_test_vals = values[0]
dtypes = dict()


print(str(values))
# insert(table, cols, values, 'QRY_test.sql')