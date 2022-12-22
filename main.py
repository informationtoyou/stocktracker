import tkinter as tk
import requests
import json

def get_stock_price(symbol):
  API_KEY = 'YOUR-API-KEY'
  API_URL = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={"5XKRQBZFV49U5QSD"}'

  response = requests.get(API_URL)
  data = json.loads(response.text)

  return data['Global Quote']['05. price']

def update_stock_price():
  price = get_stock_price('YOUR-STOCK-QUOTE')
  label['text'] = f'Price: {price}'

root = tk.Tk()
root.title('Stock Tracker')

label = tk.Label(root, text='Fetching stock price...')
label.pack()

update_button = tk.Button(root, text='Update', command=update_stock_price)
update_button.pack()

root.mainloop()
