print("\t\"Perries Cafe\"")
#Created a list to show items sold in the cafe which were stored in the variable called 'menu'
menu = ["Coffee", "Cupcake", "Tea", "Muffin"]
#Created a dictionary to store the stock value for each item on the menu
stock = {"Coffee": 10,
         "Cupcake": 20,
         "Tea": 10,
         "Muffin": 15
         }
#Another dictionary to store the price of each item on the menu 
price = {"Coffee": 7.80,
         "Cupcake": 4.20,
         "Tea": 6.45,
         "Muffin": 4.50
         }
#Calculate the total stock worth
total_stock = sum(stock[item] * price[item] for item in menu)
#Print the result
print(f"The total stock worth in the cafe is £{total_stock:.2f}")



