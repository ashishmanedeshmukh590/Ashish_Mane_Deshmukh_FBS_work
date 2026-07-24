##11.Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.


amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    count = amount // note
    if count > 0:
     print(note, "notes:", count)
     amount = amount % note