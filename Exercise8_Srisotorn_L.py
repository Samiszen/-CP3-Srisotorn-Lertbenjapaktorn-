# Set the price
IcedAmericano = 120
PureMatcha = 150
HotChocolate = 140

username = input("Username:")
password = input("Password:")

if username == "Starbuck_Coffee" and password == "morningcoffee_123":
    print("--------------------------------------------------")
    print("Welcome to Starbucks_Coffee what would you like to order?")
    print("--------------------------------------------------")

    print("1. Iced Americano 120 THB")
    print("2. Pure matcha    150 THB")
    print("3. Hot chocolate. 140 THB")

    print("--------------------------------------------------")

    order1 = int(input("Please type in the number of menu you want:"))
    glass1 = int(input("And for how many do you want for your order?:"))
    print("--------------------------------------------------")

    # Order 1
    if order1 == 1:
        total1 = IcedAmericano * glass1
        print("1. IcedAmericano for", glass1)
        print(total1, "THB")
    if order1 == 2:
        total1 = PureMatcha * glass1
        print("1. Pure matcha for", glass1)
        print(total1,"THB")
    if order1 == 3:
        total1 = HotChocolate * glass1
        print("1. Hot chocolate for", glass1)
        print(total1, "THB")

    print("--------------------------------------------------")

    # Order 2
    order2 = int(input("And for 2nd order please?, (If you don't want your 2nd order. please type 0):"))
    if order2 == 1:
        glass2 = int(input("And for how many do you want for your order?:"))
        total2 = IcedAmericano * glass2
        print("2. IcedAmericano for", glass2)
        print(total2, "THB")
    if order2 == 2:
        glass2 = int(input("And for how many do you want for your order?:"))
        total2 = PureMatcha * glass2
        print("2. Pure matcha for", glass2)
        print(total1, "THB")
    if order2 == 3:
        glass2 = int(input("And for how many do you want for your order?:"))
        total2 = HotChocolate * glass2
        print("2. Hot chocolate for", glass2)
        print(total2, "THB")
    if order2 == 0:
        total2 = 0

    # สรุป Order
    print("==================================================")
    print("All to pay is",total1 + total2, "THB")
    print("Thanks for coming to Starbuck_Coffee services enjoy your coffee order")
    print("==================================================")
else:
    print("username or password incorrect, please try again")
