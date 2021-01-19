from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import cb_tools

cg = CoinGeckoAPI()

#list tokens
l = ['bitcoin',
     'ethereum',
     'litecoin',
     'bitcoin-cash',
     'chainlink',
     'stellar',
     'eos',
     'tezos',
     'havven',
     'cosmos']

#get data from cg
btc = cb_tools.getdata_max('bitcoin', 'usd')
eth = cb_tools.getdata_max('ethereum', 'usd')
ltc = cb_tools.getdata_max('litecoin', 'usd')
bch = cb_tools.getdata_max('bitcoin-cash', 'usd')
link = cb_tools.getdata_max('chainlink', 'usd')
xlm = cb_tools.getdata_max('stellar', 'usd')
eos = cb_tools.getdata_max('eos', 'usd')
xtz = cb_tools.getdata_max('tezos', 'usd')
snx = cb_tools.getdata_max('havven', 'usd')
atom  = cb_tools.getdata_max('cosmos', 'usd')

#make a df
df = pd.DataFrame()

#fill df
df['Bitcoin'] = btc.prices['2021-01-05':]
df['Ethereum'] = eth.prices['2021-01-05':]
df['Litecoin'] = ltc.prices['2021-01-05':]
df['Bitcoin Cash'] = bch.prices['2021-01-05':]
df['Chainlink'] = link.prices['2021-01-05':]
df['Stellar'] = xlm.prices['2021-01-05':]
df['EOS'] = eos.prices['2021-01-05':]
df['Tezos'] = xtz.prices['2021-01-05':]
df['Synthetix'] = snx.prices['2021-01-05':]
df['Cosmos'] = atom.prices['2021-01-05':]