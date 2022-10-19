from tqdm import tqdm
import pandas as pd 

def simulate_single_position(market_price, price_change, number_of_simulations, short_position_size=None, long_position_size=None):
	if short_position_size:
		entry_position_value = short_position_size*market_price
	if long_position_size:
		entry_position_value = long_position_size*market_price

	for simulation in range(number_of_simulations):
		if short_position_size:
			position_value = short_position_size*market_price
			if price_change < 0:
				if position_value == entry_position_value:
					print(f"Your entry position is ${entry_position_value}")
				else:
					gain = position_value - entry_position_value	
					print(f"The value of your short position is ${position_value} and your gain is +${gain}")
				market_price = market_price - price_change	
			else:
				if position_value == entry_position_value:
					print(f"Your entry position is ${entry_position_value}")
				else:
					exposure = position_value - entry_position_value	
					print(f"The value of your short position is ${position_value} and your exposure is -${abs(exposure)}")
				market_price = market_price - price_change			
		if long_position_size:
			position_value = long_position_size*market_price
			if price_change > 0:
				if position_value == entry_position_value:
					print(f"Your entry position is ${entry_position_value}")
				else:
					gain = position_value - entry_position_value	
					print(f"The value of your long position is ${position_value} and your gain is +${gain}")
				market_price = market_price + price_change
			else:
				if position_value == entry_position_value:
					print(f"Your entry position is ${entry_position_value}")
				else:
					exposure = position_value - entry_position_value	
					print(f"The value of your long position is ${position_value} and your exposure is -${abs(exposure)}")
				market_price = market_price + price_change

	return "Simulation complete"

# simulate_single_position(1937, 10, 20, long_position_size=100)
margin = None
equity = None

def simulate_hedged_position(opening_price, position_size, closing, long_position=True, high=None, low=None, margin=None, leverage=None):
	# if long_position is set to true, the market position is bullish and bearish when long_position is set to false
	# closing here represent a list containing periodic market closing prices on the instrument
	# high and low represent the market highs and lows for the instrument
	# this is a market simulation on a given position within a given period of time
	# simulating how market price fluctuations affect positions in a portfolio
	entry_position = opening_price*position_size
	position_hedge = entry_position
	current_contract_value = entry_position
	if margin and leverage:
		required_margin = entry_position/leverage
		available_margin = margin - required_margin
		equity = margin
		hedge_margin = available_margin
		hedge_equity = margin
	print(f"Entry position value: ${entry_position}\nHedge position value: ${position_hedge}\nMarket price:${opening_price}\nRequired_margin: ${required_margin}\nAvailable_margin: ${available_margin}\nEquity: ${equity}\nLeverage: {1}:{leverage}")
	for price in tqdm(closing):
			# entry_position = current_contract_value
			current_contract_value = price*position_size
			position_gain = current_contract_value - entry_position
			if long_position:
				hedge_position_value = position_hedge - position_gain
				available_margin = available_margin + position_gain
				equity = equity + position_gain
				hedge_margin = hedge_margin-position_gain
				hedge_equity = hedge_equity - position_gain
				if position_gain < 0:
					print(f'Long position value: ${current_contract_value}\nNet gain/loss: -${abs(position_gain)}\nHedge position value: ${hedge_position_value}\nMarket price:${price}')
					print(f"Available margin: ${available_margin}\nEquity: ${equity}")
					print(f"Hedge margin: ${hedge_margin}\nHedge equity: ${hedge_equity}")
					print('*******************************************************************************************************************************')
				else:	
					print(f'Long position value: ${current_contract_value}\nNet gain/loss: +${position_gain}\nHedge position value: ${hedge_position_value}\nMarket price:${price}')
					print(f"Available margin: ${available_margin}\nEquity: ${equity}")
					print(f"Hedge margin: ${hedge_margin}\nHedge equity: ${hedge_equity}")
					print('*******************************************************************************************************************************')

				position_value = current_contract_value
			else:
				short_position_value = entry_position - position_gain
				hedge_position_value = current_contract_value
				available_margin = available_margin-position_gain
				equity = equity-position_gain
				hedge_margin = hedge_margin + position_gain
				hedge_equity = hedge_equity + position_gain
				if position_gain < 0:
					print(f'Short position value: ${short_position_value}\nNet gain/loss: +${abs(position_gain)}\nHedge position value: ${hedge_position_value}\nMarket price:${price}')
					print(f"Available margin: ${available_margin}\nEquity: ${equity}")
					print(f"Hedge margin: ${hedge_margin}\nHedge equity: ${hedge_equity}")
					print('*******************************************************************************************************************************')
				else:	
					print(f'Short position value: ${short_position_value}\nNet gain/loss: -${position_gain}\nHedge position value: ${hedge_position_value}\nMarket price:${price}')
					print(f"Available margin: ${available_margin}\nEquity: ${equity}")
					print(f"Hedge margin: ${hedge_margin}\nHedge equity: ${hedge_equity}")
					print('*******************************************************************************************************************************')

				position_value = short_position_value
	position_return = (position_value - required_margin)/entry_position*100
	hedge_return = (hedge_position_value - position_hedge)/position_hedge*100
	print(f'Portfolio return, {position_return}% and hedge position return {hedge_return}%')

data = pd.read_excel('datasets/Weekly Gold prices.xlsx')
# data.dropna(inplace=True)
prices = list(data['High'].values)
opening = data['Open'].values[0]
for n in range(4):
	prices.pop()
simulate_hedged_position(opening, 10 , prices, long_position=True, margin=10000, leverage=1000)
    