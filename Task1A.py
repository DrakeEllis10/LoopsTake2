# Write a program that will ask a user for a number of grocery items. Then, write a
# loop that will accept that many grocery items. You do not have to store the items.
# For example, if the user enters 3, the program should allow the user to enter 3 items.

number = int(input("How many items do you need?"))
i = 0
while i < number:
    input("What is the item? ")
    i = i + 1