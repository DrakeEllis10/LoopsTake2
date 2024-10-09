# Use a loop that prints the square and cube of a number.
# The table should look like:
# n  |  n^2  |  n^3
# ___________________
#  0     0      0
#  1     1      1
#  2     4      8
#  3     9      27

numbers = int(input("How many numbers? "))
print("n   |   n^2   |   n^3 ")
print("-----------------------")
i = 0
while i < numbers:
    print(i, "    ", i * i, "    ", i * i * i)
    i = i + 1
