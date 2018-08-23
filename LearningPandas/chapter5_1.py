import pandas as pd
import numpy as np
from pandas import Series,DataFrame

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
#print(obj2)
#print(obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0))
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])

import pandas.io.data as web
