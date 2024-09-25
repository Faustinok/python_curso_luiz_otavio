"""bla"""
# https://c\docs.python.org/3/library/datetime.html
from datetime import datetime

data_str_data = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'
data = datetime(2022, 4, 4, 7, 45, 36)
data2 = datetime.strptime(data_str_data, data_str_fmt)
print(data)
print(data2)