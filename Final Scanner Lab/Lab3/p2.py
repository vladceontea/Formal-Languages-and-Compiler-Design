
read(n).
prime <- 1.

if (n < 2):
    prime <- 0.
elif (n = 2):
    prime <- 1.
else:
    prime <- 1.
for (i<-2, i<n, i<-i+1):
    if(n%i) = 0:
        prime <- 0.
        i <- n.

if (prime = 0).
    show("Not_" + "a_" + "prime_" + "number").
else:
    show("Prime_" + "number_").

