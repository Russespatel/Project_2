amount = int(input( "Please enter an amount in cents less than a dollar (1-99): " ))

Quarters = (amount // 25)
Dime = (amount % 25 // 10)
Nickles = (amount % 25 % 10) // 5
Pennies = (amount % 25 % 10 % 5) //1

print("Your Change Will Be")
print(
    "Quarters =",Quarters,
    "Dime =",Dime,
    "Nickles =",Nickles,
    "Pennies =",Pennies)