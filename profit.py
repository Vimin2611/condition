buying = int(input("Enter the actual cost of the product :"))
selling = int(input("Enter the price you are selling at:"))
if (buying < selling) :
    amount = selling - buying
    print("Total amount of profit =", amount)
else :
    print("No profit made !")
 