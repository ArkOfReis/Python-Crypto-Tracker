import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import pyplot
import mplfinance as mpf
from tkinter import *
from PyQt5 import QtGui
import os

import datetime as dt

crypto = "BTC"
currency = "USD"

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)
ada = web.DataReader(f"ADA-{currency}", "yahoo", start, end)

plt.figure(num='Crypto Tracker  |  Version 1.2.1')
PATH_TO_ICON = os.path.dirname(__file__) + ''
plt.get_current_fig_manager().window.setWindowIcon(QtGui.QIcon(PATH_TO_ICON))

plt.rcParams['axes.facecolor'] = 'black'
plt.yscale("log")

plt.title("Crypto Price Chart")

plt.plot(btc['Close'], label="BITCOIN")
plt.plot(eth['Close'], label="ETHEREUM")
plt.plot(ada['Close'], label="CARDANO")
plt.legend(facecolor='k', labelcolor='w', loc="upper left")

plt.show()