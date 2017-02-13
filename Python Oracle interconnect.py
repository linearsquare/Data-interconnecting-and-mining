import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('oracle://kangguangliang1:yhd123,@bi_exadata')
data = pd.read_sql_query('select * from table_name', engine)


def utf(x):
    if not isinstance(x, unicode):
        try:
            return str(x).decode('utf-8')
        except UnicodeDecodeError:
            return x
    else:
        return x 

def utfs(x):
    cols = x.dtypes[x.dtypes=='object'].index
    for i in cols:
        x[i] = x[i].map(utf)
    return x

workbook = pd.ExcelWriter(datetime.now().strftime('%Y%m%d')+u' table_name.xlsx', options={'encoding':'utf-8'})
utfs(data).to_excel(workbook, sheet_name=u'sheet1', index=False)                                                
workbook.save()