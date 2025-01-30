from model import *
from statistic import *
from client import *

#import questionary as qu


def open_account(api_key, secret_key, paper, name):
    global account
    Client.API_KEY = api_key
    Client.SECRET_KEY = secret_key
    Client.paper = paper
    account = Client(name = f'{name}')
    return account

def get_account(name):
    for a in account.stack:
        if a.name == name:
            print(f"[>][Selected Account: {a.name}]")
            return a

def del_account(name):
    for a in account.stack:
        if a.name == name:
            account.stack.remove(a)
            print(f"[!][Deleted Account: {a.name}]")
            return a

def task(symbol, type):
    account.info()
    
    if isinstance(symbol, str):  # If symbol is a single string, convert it to a list
        symbol = [symbol]
    #for loop of focus array
    for sym in symbol:
        account.focus(sym)
        hist_data = account.history(type, time = 0.3, step = 5)
        
        data = Statistic(sym, hist_data)
        data.create()

        data.graph()

    #for loop of focus array
    #get file name 
    #live_data = account.stream(symbol)
    
    #for sym in symbol:
        #live = [asyncio.create_task(market.stream(sym))]
    # Run all tasks concurrently
    #await asyncio.gather(*live)

def main():
    
    #initialized start screen
    #create/get account
    
    api_key = "PKE1B8WAV2KJ324ZKQKC"
    secret_key = "Ro7nFRclHQekQSf5Tt3zbpJAr9AaXhQ7r67sJJDy"
    paper = True
    name = 'Random_123'

    # api_key = qu.password("API Key:", qmark= "[>]").ask()
    # secret_key = qu.password("Secret Key:", qmark= "[>]").ask()
    # paper = qu.confirm("Paper:", qmark= "[>]").ask()
    # name = qu.text("Name:", qmark= "[>]").ask()
    #check to verify keys

    account = open_account(api_key=api_key, secret_key=secret_key, paper=paper, name=name)
    #option and parameter
        #symbol
        #start date(scroll bar + hard input)
        #label(bar, close, etc)

    symbol = "BTCUSD", "ETHUSD"
    task(symbol, type = "BAR")

    #=>async data(option, parameter)
        #gather history
        #stream live data

    #=>async model(gather history, live data )
        #process data
        #train model
        #return value(prediction) 

    #=>plot(data() -> history) && (data -> live data == idel && model -> prediction)

    #[automate buy and sell request]
        #buget(account total)
        #request(stock amt, price amt)
        

    return True
if __name__ == "__main__":
    main()

