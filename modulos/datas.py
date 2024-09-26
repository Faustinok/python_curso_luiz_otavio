"""bla"""
# https://c\docs.python.org/3/library/datetime.html
from datetime import datetime
from pytz import timezone
# data vinda de uma string
data_str_data = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'
data2 = datetime.strptime(data_str_data, data_str_fmt)
# criando uma data com ints
data = datetime(2022, 4, 4, 7, 45, 36)
##############################

# agora
print(datetime.now())
print(data)
print(data2)

# TIMEZONE
print('timezones')
print(datetime.now(timezone('America/Sao_Paulo')))
print(datetime.now(timezone('Asia/Tokyo')))

# UNIX
print('timestamp')
time_stamp = datetime.now().timestamp()
print(time_stamp)
print('data a partir do timestamp ')
print(datetime.fromtimestamp(time_stamp))


# comparando datas
fmt = '%d/%m/%Y %H:%M:%S'
d1 = datetime.strptime('23/07/1996 10:00:00', fmt)
d2 = datetime.strptime('23/07/2024 10:00:00', fmt)
print(d1 > d2)
print(d2 > d1)

# delta datetime
print(d2 - d1)
delta = d2 - d1
print(delta)

# formatar datas

fmt2 = '%d/%m/%Y'
d3 = datetime.now()
print(datetime.strftime(d3, fmt2))
