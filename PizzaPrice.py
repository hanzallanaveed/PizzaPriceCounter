print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
M_L_bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill+= 2
    if extra_cheese == "Y":
        bill+= 1
    print (f"Your final bill is ${bill}")

if size == "M":
    M_L_bill = 20
    if add_pepperoni == "Y":
        M_L_bill+= 3
    if extra_cheese == "Y":
        M_L_bill+= 1
    print (f"Your final bill is ${M_L_bill}")

if size == "L":
    M_L_bill = 25
    if add_pepperoni == "Y":
        M_L_bill+= 3
    if extra_cheese == "Y":
        M_L_bill+= 1
    print (f"Your final bill is ${M_L_bill}")


if extra_cheese == "Y":
    M_L_bill+= 1
