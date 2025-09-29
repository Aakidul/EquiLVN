"""
OE = THE SWING HIGH EQUILIBRIUM
E = THE SWING LOW EQUILIBRIUM
S = SUPPORT
R = RESISTANCE
W = WINDOW LENGTH(NUMBERS OF CANDLES)
M = MIDPOINT[MIDPOINT OF WINDOW, FORMULA IS (S+R)/2 ]
T = TARGET FOR PROFIT, FORMULA IS (PERCENTAGE/100)*VALUE
"""

#next fetch candles and find E and OE and S AND R, use pandas and create new functions.




Input_symbol = input('ENTER SYMBOL example: BTCUSDT etc,  :- ')

API_KEY = ""
API_SECRET = ""
GLOBAL_TOKEN_SYMBOL = str(Input_symbol.upper())

from binance.client import Client
import time
import pandas as pd



CLIENT = Client(API_KEY, API_SECRET)


def get_candles():
    CANDLES = CLIENT.get_klines(symbol=GLOBAL_TOKEN_SYMBOL, interval=CLIENT.KLINE_INTERVAL_1MINUTE, limit=1000)
    df = pd.DataFrame(CANDLES, columns=[
'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close-time',
'quote-asset-volume', 'numbers-of-strades', 'taker-buy-base', 'taker-buy-quote', 'ignore'
])
    for col in df:
        df[col] = pd.to_numeric(df[col], errors='coerce')


    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def market_zone_analysis(df):
    lows = df['low'].tolist()
    highs = df['high'].tolist()
    lows.sort()
    highs.sort()


    support = lows[0]
    resistance = highs[-1]
    midpoint = (support + resistance) / 2



    zone1_rows = [] #candle data from support to midpoint
    zone2_rows = [] #candle data from midpoint to resistance

    #looping for each candles to find candles between zone1 to zone2
    for idx, row in df.iterrows():

        price = row['close']

        if support <= price <= midpoint:
            zone1_rows.append(row)

        elif midpoint <= price <= resistance:
            zone2_rows.append(row)


    zone1 = pd.DataFrame(zone1_rows)
    zone2 = pd.DataFrame(zone2_rows)
    sorted_zone1 = zone1.sort_values(by='quote-asset-volume', ascending=True)
    sorted_zone2 = zone2.sort_values(by='quote-asset-volume', ascending=True)
    LVN1 = sorted_zone1.iloc[0]['high'] #LEAST VOLUME NODE , FROM SUPPORT TO MIDPOINT
    LVN2 = sorted_zone2.iloc[0]['low']  #LEAST VOLUME NODE, FROM MIDPOINT TO RESISTANCE



    sentiment = []
    if sorted_zone1.iloc[0]['quote-asset-volume'] > sorted_zone2.iloc[0]['quote-asset-volume']:
        sentiment.append('BULLISH')

    elif sorted_zone1.iloc[0]['quote-asset-volume'] < sorted_zone2.iloc[0]['quote-asset-volume']:
        sentiment.append('BEARISH')

    else:
        sentiment.append('NONE')


    LVN1 = float(LVN1)
    LVN2 = float(LVN2)


    return [support, resistance, midpoint, LVN1, LVN2, sentiment[0]]

df = get_candles()
GLOBAL_MARKET_DATA = market_zone_analysis(df)






def price_get():
    PRICE = CLIENT.get_symbol_ticker(symbol=GLOBAL_TOKEN_SYMBOL)
    return float(PRICE['price'])


GLOBAL_PRICE = price_get()


def main(market_data, price):
    print('''


 ▄▄▄      ▄▄▄       ██ ▄█▀ ██▓▓█████▄  █    ██  ██▓    
▒████▄   ▒████▄     ██▄█▒ ▓██▒▒██▀ ██▌ ██  ▓██▒▓██▒    
▒██  ▀█▄ ▒██  ▀█▄  ▓███▄░ ▒██▒░██   █▌▓██  ▒██░▒██░    
░██▄▄▄▄██░██▄▄▄▄██ ▓██ █▄ ░██░░▓█▄   ▌▓▓█  ░██░▒██░    
 ▓█   ▓██▒▓█   ▓██▒▒██▒ █▄░██░░▒████▓ ▒▒█████▓ ░██████▒
 ▒▒   ▓▒█░▒▒   ▓▒█░▒ ▒▒ ▓▒░▓   ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░
  ▒   ▒▒ ░ ▒   ▒▒ ░░ ░▒ ▒░ ▒ ░ ░ ▒  ▒ ░░▒░ ░ ░ ░ ░ ▒  ░
  ░   ▒    ░   ▒   ░ ░░ ░  ▒ ░ ░ ░  ░  ░░░ ░ ░   ░ ░   
      ░  ░     ░  ░░  ░    ░     ░       ░         ░  ░
                               ░                       


[+] Warning: This script generates trade signals based on historical data. Use for reference only — do not follow blindly. Not responsible for any financial losses.

 ''')



    print(f'MARKET DATA FOR {GLOBAL_TOKEN_SYMBOL}...>')
    print('\n')
    print(f'SUPPORT:- {market_data[0]}')
    print(f'RESISTANCE:- {market_data[1]}')
    print(f'MIDPOINT:- {market_data[2]}')
    print(f'LVN1:- {market_data[3]}')
    print(f'LVN2:- {market_data[4]}')
    print(f'SENTIMENT:- {market_data[5]}')
    print('\n')
    print('\n')
    print('TRADE SIGNAL....>')
    if market_data[5] == 'BULLISH':
        print(f'PAIR TYPE:- {GLOBAL_TOKEN_SYMBOL}')
        print('TRADE TYPE:- BUY LONG')
        print(f'ENTRY:- {market_data[3]}')
        print(f'STOP LOSS:- {market_data[0]}')
        print(f'TAKE PROFIT:- {market_data[1]}')
    elif market_data[5] == 'BEARISH':
        print(f'PAIR TYPE:- {GLOBAL_TOKEN_SYMBOL}')
        print('TRADE TYPE:- SELL SHORT')
        print(f'ENTRY:- {market_data[4]}')
        print(f'STOP LOSS:- {market_data[1]}')
        print(f'TAKE PROFIT:- {market_data[0]}')

    else:
        print('NO SIGNAL FOR NOW')

result_list = main(GLOBAL_MARKET_DATA, GLOBAL_PRICE)
print(result_list)

