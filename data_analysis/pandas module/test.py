import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
df11=pd.DataFrame({'dept':['A','A','B','B','B'],'salary':[10,20,30,40,50]})
df11['dept_avg']=df11.groupby('dept')['salary'].transform('mean')
print(df11)