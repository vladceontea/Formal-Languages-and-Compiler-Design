
# Compute max of 3 numbers with errors

*a <- read("Enter first number: ") #This is a lexical error because the identifier starts with a symbol, which is not allowed.
b -> read("Enter second number: ") #This is a lexical error because the assignment operator is wrong.
c <- read("Enter third number: ")

iff a >= b and a >= c:
    maxim <- a
eliff b >= a and b >= c:
    maxim <- b
else:
    maxim <- c

show("The biggest number is " + text(maxim))

