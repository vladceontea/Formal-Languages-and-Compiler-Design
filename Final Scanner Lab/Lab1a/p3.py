
# Compute the sum of n numbers

n <- read("Enter the number of numbers you wish to compute the sum of: ")
sum <- 0

for i in range(0, n):
    x <- int(input("Enter the next number: "))
    sum <- sum + x

show("The sum is " + text(sum))