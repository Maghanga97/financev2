import random
import pandas as pd

current_price = 1819
product = 'Gold'
estimates = [random.randint(1000, 2000) for x in range(20)]
long_position = [estimate-current_price for estimate in estimates]
short_position = [current_price-estimate for estimate in estimates]

data = {'simulated price':	estimates, 'Long P/L': long_position, 'Short P/L': short_position}
instrument = {'Financial instrument': product, 'Market Price': current_price}
data_frame = pd.DataFrame(data)
instrument_frame = pd.DataFrame(instrument)
print(data_frame)