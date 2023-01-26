#Write your code here.
try:
    price = float(input())
    vat = float(input())
    vat_amount = price * (vat/100)
    total_price = price + vat_amount
    print(round(total_price))
except:
    print("Invalid Input")
