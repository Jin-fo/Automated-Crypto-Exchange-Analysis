import os
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from datetime import datetime

class Statistic:
    data = None
    symbol = str

    def __init__(self, symbol, data):
        self.data = data
        self.file_name = symbol

    def create(self):#create and delete file by focus
        self.data.to_csv(f"{self.file_name}.csv")
        print(f"\t - Recorded: {self.file_name}")
        
    def read(self):
        data = pd.read_csv(f'{self.file_name}.csv')
        data = pd.DataFrame({
            'Date': pd.to_datetime(data['timestamp']),
            'Close': data['close']
            #open
            #low
            #high
        })
        os.remove(f'{self.file_name}.csv')
        data.to_csv(f'{self.file_name}_mod.csv', index = False)
        return data
    
    def append(self, data):
        field = [i[0] for i in data]
        data = {i[0]: i[1] for i in data}
        #print(data) returns
        #{'symbol': 'ETH/USD', 'timestamp': datetime.datetime(2024, 8, 11, 21, 56, tzinfo=datetime.timezone.utc), 'open': 2577.44, 'high': 2579.215, 'low': 2577.44, 'close': 2579.215, 'volume': 0.0, 'trade_count': 0.0, 'vwap': 0.0}
        #NOT POSSIBLE FOR print(data.symbol)
        with open(f"{self.file_name}.csv", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = field)
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

    def format_graph(self, title, xlabel, ylabel, grid=True):
        plt.style.use("dark_background")
        plt.figure(figsize=(8, 5))

        plt.style.context({
            'lines.linewidth': 1.0, 
            'axes.facecolor': 'black',     
            'axes.grid': grid,             # Enable grid
            'grid.color': '#D3D3D3',       # Light gray grid lines
            'legend.fontsize': 10,      # Smaller legend font
            'legend.frameon': True,     # Frame around legend
            'legend.framealpha': 0.9,   # Slight transparency for legend frame
            'legend.fancybox': True,    # Rounded box for legend
        })
        
        plt.title(title, fontsize=18, fontweight='bold', loc='left')
        plt.xlabel(xlabel, fontsize=10)
        plt.ylabel(ylabel, fontsize=10)
        plt.xticks(rotation=0, ha='right', fontsize=8)

        if grid:
            plt.grid(True, linestyle='--', alpha=0.7)

    def graph(self):  
        self.format_graph(
            title   = f"{self.file_name} Price",
            xlabel  = 'Date', 
            ylabel  = 'Close Price ($)') 
        
        data = self.read()
        #check correct naming convention
        x = data['Date']
        y_close = data['Close']

        plt.plot(x, y_close, label='Close', color='lime')
        #high, low etc
        print(f"\t - Graphed:  {self.file_name}")

        plt.tight_layout()
        plt.legend(loc='best') 
        plt.savefig(f"{self.file_name}.png")
        plt.show(block=False)

