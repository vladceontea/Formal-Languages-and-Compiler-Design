
# Verify if number is prime

n <- read("Enter the number: ")
prime <- 1

iff n < 2:
    prime <- 0
eliff n = 2:
    prime <- 1
else:
    prime <- 1
    for i in range(2, n):
        iff(n % i) = 0:
            prime <- 0
            i <- n

iff prime = 0:
    show("Not a prime number")
else:
    show("Prime number")

