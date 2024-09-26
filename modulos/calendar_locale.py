import calendar
import locale

print(calendar.calendar(2024))
# locale muda o idioma para o padrao do sistema operacional
locale.setlocale(locale.LC_ALL, '')
print(calendar.calendar(2024))
# pegar o ultimo dia de um mes
# print(calendar.monthrange(2024, 10))

print(locale.getlocale())
