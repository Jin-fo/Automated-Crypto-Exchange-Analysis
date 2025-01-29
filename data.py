
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from asyncio import streams

from alpaca.data.live.crypto import *
from alpaca.data.historical.crypto import *
from alpaca.data.live.stock import *
from alpaca.data.historical.stock import *

#from alpaca.data.live.option import *
#from alpaca.data.historical.option import *

from alpaca.data.requests import *
from alpaca.data.timeframe import *
from alpaca.trading.client import *
from alpaca.trading.stream import *
from alpaca.trading.requests import *
from alpaca.trading.enums import *
from alpaca.common.exceptions import APIError

def time_now(country = "America", city = "New_York"):
    time = datetime.now(ZoneInfo(f"{country}/{city}"))
    return time

class Account:
    #stack = [] mutiple account
    API_KEY = str
    SECRET_KEY = str
    name = str

    paper = bool
    position = None

#quick-start function

#open the account using the API Key
    def __init__(self, name):
        self.name = name
        self.client = TradingClient(api_key=Account.API_KEY, secret_key=Account.SECRET_KEY, paper=Account.paper)
        self.position = self.client.get_all_positions()
        self.account = self.client.get_account()

        self.symbol = None
        print("[o][Account Linked Successfully]")

    def show_symbol(self, exchange):
        #exchange value: stock, crypto, etc
        #show a list of existing ticket
        return None
    
    def focus(self, symbol):
        print(symbol)
        error = False
        try:
            self.symbol = self.client.get_asset(symbol_or_asset_id=symbol)
        except APIError as e:
            print(f"[!][{e}]")
            return None
            # error = True, re-reference

        print(f'[o][Focus: {self.symbol.symbol}]')
        return self.symbol
    
    def history(self, type, time, step): 
        now = time_now()
        data = BaseBarsRequest(
            symbol_or_symbols = self.symbol.symbol,
            timeframe = TimeFrame(amount = step, unit = TimeFrameUnit.Minute),
            start = now - timedelta(days = time),
            limit = 1000000
        )
        if self.symbol.exchange == "CRYPTO":
            if type.upper() == "BAR":
                crypto_history = CryptoHistoricalDataClient(api_key=Account.API_KEY, secret_key=Account.SECRET_KEY)
                bar = crypto_history.get_crypto_bars(data).df

        elif self.symbol.exchange != "CRYPTO":
            if type.upper() == "BAR":
                stock_history = StockHistoricalDataClient(api_key=Account.API_KEY, secret_key=Account.SECRET_KEY)
                bar = stock_history.get_stock_bars(data).df

        else:
            print("[!][INVALID Exchange Type Error]")
            return None
        
        print(f"[o][{type.upper()} History from {time} days, by {step} minutes]")
        return bar 
    
        file_name = to_string(symbol.symbol)
        bar.to_csv(f"{file_name}.csv")
        print(f"\t - Recorded: {file_name}")
        self.plot(file_name)
        print(f"\t - Graphed:  {file_name}")
        return bar
    
    #stream the crypto of its latest bar
    def stream(self, symbol):
        print("[o][BAR Stream]")
        if symbol.exchange == 'CRYPTO':
            url = BaseURL.MARKET_DATA_STREAM.value + "/v1beta3/crypto/" + CryptoFeed.US

        elif symbol.exchange != 'CRYPTO':
            url = BaseURL.MARKET_DATA_STREAM.value + "/v2/" + DataFeed.IEX
            
        stream = DataStream(url, self.API_KEY, self.SECRET_KEY)
        stream._subscribe(handler=self.on_update, symbols=(symbol.symbol,), handlers=stream._handlers["bars"])

        print("[~][Retriving...]")
        stream.run()

    async def on_update(self, data):
        return data
    


        #print(data) returns:
        #symbol='ETH/USD' timestamp=datetime.datetime(2024, 8, 11, 21, 52, tzinfo=datetime.timezone.utc) open=2575.145 high=2576.995 low=2575.145 close=2576.995 volume=0.0 trade_count=0.0 vwap=0.0
        file_name = to_string(data.symbol)

        try:
            self.append(file_name, data)
            print(f"\t - Appended: {file_name}")
        except FileNotFoundError as e:
            self.create(file_name)
            print(f"{e}")

        self.plot(file_name)
        print(f"\t - Graphed:  {file_name}")

        print("[~][Retriving...]")

    




    #order, not implemented 
    def order(self, side, qty): #buy in stock, +buy in dollar
        print(f"[o][Ordered: ", end = '')
        if side == "BUY":
            print(f"+{qty}]")
        elif side == "SELL":
            print(f"-{qty}]")
    

    def info(self):
        print(f"\t name: {self.name}")
        # array = [s.symbol for s in self.position]
        print(f"\t position: {[s.symbol for s in self.position]}")
        print(f"\t equity: {self.account.equity}")
        print(f"\t cash: {self.account.cash}")
        print(f"\t time: {time_now()}")
        