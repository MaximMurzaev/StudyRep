import pandas as pd
import requests
from matplotlib import pyplot as plt
# from pprint import pprint

# Запрос данных с по котировкам акций ПАО Лукойл за 14.01.2025 часовой таймфрейм
quotes = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/LKOH/candles.json?from=2025-01-14&till=2025-01-14&interval=60').json()
# pprint(quotes)

# Получаем список с необходимыми данными для построения графика
data = [{k : r[i] if k != 'begin' else r[i][11 : 16] for i, k in enumerate(quotes['candles']['columns'])} for r in quotes['candles']['data']]
# pprint(data)

# Преобразуем данные из json в таблицу
frame = pd.DataFrame(data)
print(frame)

# Выводим график
plt.figure(figsize=(15, 6), num='LKOH')
plt.plot(list(frame['begin']), list(frame['close']), color='blue')
plt.xlabel('Time')
plt.ylabel('Price (RUR)')
# plt.savefig("shares.png")
plt.show()