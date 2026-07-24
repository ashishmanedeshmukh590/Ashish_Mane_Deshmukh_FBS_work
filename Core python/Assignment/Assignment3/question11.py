##11.Accept age of five people and also per person ticket amount and then calculate total 
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discountc. Others need to pay full.

total = 0

for i in range(5):
    age = int(input("Enter Age: "))
    ticket = float(input("Enter Ticket Amount: "))

    if age < 12:
        ticket = ticket * 0.70
    elif age > 59:
        ticket = ticket * 0.50

    total += ticket

print("Total Ticket Amount =", total)
