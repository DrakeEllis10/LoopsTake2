# Build an app that will take a positive integer input and run a loop that prints
# "This is silly" that number of times. For example, if a user enters 3, the output is:
# This is silly
# This is silly
# This is silly

number = int(input("How many times? "))
i = 0
while i < number:
    print("This is silly")
    i = i + 1
