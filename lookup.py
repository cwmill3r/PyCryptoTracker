from tkinter import *
import requests
import json
import os
os.system('cls')
###############################################

root = Tk()

root.title("Crypto Currency Portfolio")
#root.iconbitmap(r' c:codemy.ico') # can have an icon

## ************ CREATE HEADER *****************
#header = ["Name", "Rank", "Current Price", "Price Paid", "P/L Per", "1-Hour Change", "24-Hour Change", "7-Day Change", Current]

header_name = Label(root, text=head, bg="white", font="Verdana 8 bold")
header_name.grid(row=0, column=column_count, sticky=N+S+E+W)


#root.mainloop()

api_requests = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_requests.content)

portfolio_profit_loss = 0

print("------------------------------------")

def lookup():
	# My Portfolio
	my_portfolio = [
		{
			"sym": "BTC",
			"amount_owned": 1,
			"price_paid_per": 6400
		},
		{
			"sym": "ETH",
			"amount_owned": 20,
			"price_paid_per": 380
		},
		{
			"sym": "XMR",
			"amount_owned": 20,
			"price_paid_per": 160
		},
		{
			"sym": "LTC",
			"amount_owned": 5,
			"price_paid_per": 200
		},
		{
			"sym": "BCH",
			"amount_owned": 5,
			"price_paid_per": 2000
		},
	]

	for x in api:
		for coin in my_portfolio:
			if coin["sym"] == x["symbol"]:

				#Do some meth
				total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
				current_value = float(coin['amount_owned']) * float(x["price_usd"])
				profit_loss = current_value - total_paid
				portfolio_profit_loss += profit_loss
				profit_loss_per_coin = float(x["price_usd"] ) - float(coin["price_paid_per"])



				print(x["name"])
				print(" Current Price: ${0:.2f}".format(float(x["price_usd"])))
				print(" Profit/Loss Per Coin: ${0:.2f}".format(float(profit_loss_per_coin)))
				print(" Rank: {0:.0f}".format(float(x["rank"])))
				print(" Total Paid: ${0:.2f}".format(float(total_paid)))
				print(" Current Value: ${0:.2f}".format(float(current_value)))
				print(" Profit/Loss: ${0:.2f}".format(float(profit_loss)))
				print("------------------------------------")

	print("Portfolio Profit/Loss: ${0:.2f}".format(float(portfolio_profit_loss)))

	



			




