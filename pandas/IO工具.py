from io import StringIO,BytesIO
import pandas as pd
'''
StringIO和BytesIO是在内存中操作str和bytes的方法，
使得和读写文件具有一致的接口。
'''
data=('col1,col2,col3\n'
       'a,b,1\n'
      'a,b,2\n'
      'c,d,3\n'
      )
print(pd.read_csv(StringIO(data)))
print(pd.read_csv(StringIO(data),usecols=lambda x: x.upper() in ['COL1','COL3']))