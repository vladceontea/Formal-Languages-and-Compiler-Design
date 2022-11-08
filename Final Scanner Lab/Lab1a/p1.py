
# Compute max of 3 numbers

a <- read("Enter first number: ")
b <- read("Enter second number: ")
c <- read("Enter third number: ")

iff a >= b and a >= c:
    maxim <- a
eliff b >= a and b >= c:
    maxim <- b
else:
    maxim <- c

show("The biggest number is " + text(maxim))


