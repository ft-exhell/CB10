from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
cg = CoinGeckoAPI()

def getdata_max(coin, currency):
    """
    Returns a DataFrame of daily history of a coin's prices, 
    market caps and volumes.
    """
    data = cg.get_coin_market_chart_by_id(coin, currency, 'max') # a list of dictionaries with data types as keys
    df = pd.DataFrame({k:dict(v) for k,v in data.items()})
    df = df.set_index(pd.to_datetime(df.index,unit='ms'))
    
    return df

def compare_to_btc(coin):
    """
    Returns history of prices of a coin.
    """
    # no need to compare bitcoin to itself
    if name != 'bitcoin':
        # dump data
        mkt_chart = cg.get_coin_market_chart_by_id(coin, 'btc', 'max')
        # prices have UNIX timestamps, convert to UTC
        for entry in mkt_chart['prices']:
            entry[0] = pd.to_datetime(entry[0], unit='ms')
        return mkt_chart['prices']
    else:
        raise ValueError('This function works only with alts.')
        
def get_exchange_volume(coin, days):
    data = cg.get_exchanges_volume_chart_by_id(coin, days)
    data_dict = {'Date':[], 'Volume':[]}
    for item in data:
        data_dict['Date'].append(item[0])
        data_dict['Volume'].append(item[1])
    df = pd.DataFrame(data_dict['Volume'], index=data_dict['Date'])
    df.index = pd.to_datetime(df.index, unit = 'ms')
    df.index = df.index.rename('Date')
    df.columns = ['Volume']
    df['Volume'] = pd.to_numeric(df['Volume'])
    
    return(df)

def reformat_large_tick_values(tick_val, pos):
    """
    Turns large tick values (in the billions, millions and thousands) such as 4500 into 4.5K and also appropriately turns 4000 into 4K (no zero after the decimal).
    """
    if tick_val >= 1000000000:
        val = round(tick_val/1000000000, 1)
        new_tick_format = '{:}B'.format(val)
    elif tick_val >= 1000000:
        val = round(tick_val/1000000, 1)
        new_tick_format = '{:}M'.format(val)
    elif tick_val >= 1000:
        val = round(tick_val/1000, 1)
        new_tick_format = '{:}K'.format(val)
    elif tick_val < 1000:
        new_tick_format = round(tick_val, 1)
    else:
        new_tick_format = tick_val

    # make new_tick_format into a string value
    new_tick_format = str(new_tick_format)
    
    # code below will keep 4.5M as is but change values such as 4.0M to 4M since that zero after the decimal isn't needed
    index_of_decimal = new_tick_format.find(".")
    
    if index_of_decimal != -1:
        value_after_decimal = new_tick_format[index_of_decimal+1]
        if value_after_decimal == "0":
            # remove the 0 after the decimal point since it's not needed
            new_tick_format = new_tick_format[0:index_of_decimal] + new_tick_format[index_of_decimal+2:]
            
    return new_tick_format