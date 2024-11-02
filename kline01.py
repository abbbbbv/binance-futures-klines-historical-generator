#print historical data to text file 

from binance.client import Client
from datetime import datetime, timedelta

client = Client('key','secret')

start_time = (datetime.now() - timedelta(days=150)).strftime("%d %b %Y %H:%M:%S")
end_time = datetime.now().strftime("%d %b %Y %H:%M:%S")

# replace btcusdt with any valid symbol
#replace  Client.KLINE_INTERVAL_5MINUTE with any valid timeframe 
klines = client.futures_historical_klines_generator("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, start_time, end_time)

# Write data to a text file
with open('btc_5month_5min_data01.txt', 'w') as file:  # change file name as needed
    for kline in klines:
        # Prepare the data point (Open Time, Open, High, Low, Close, Volume, Close Time)
        data_point = f"{kline[0]},{kline[1]},{kline[2]},{kline[3]},{kline[4]},{kline[5]},{kline[6]}"
        file.write(data_point + "\n")

print("Data has been written to the file ")
