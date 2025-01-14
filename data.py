
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

import csv
import numpy as np
import pandas as pd

class Account:
    #stack = [] mutiple account
    API_KEY = str
    SECRET_KEY = str
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