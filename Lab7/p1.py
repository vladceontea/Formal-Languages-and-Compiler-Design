
read(a)
read(b)
read(c)
read(maxim)

if (a>= b and a >= c):
    maxim <- a
elif(b >= a and b >= c):
    maxim <- b
else:
    maxim <- c

show("The_" + "biggest_" + "number_" + "is_")
show(maxim)
