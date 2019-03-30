def factorial(n) :
    product = 1
    while n > 0:
        product = product * n
        n = n - 1
    return product

n = input("Please input x:")
product = factorial(int(n))
print(product)

str = list(str(product))
#print(str)
i = -1
counter = 0
while int(str[i]) == 0:
    counter = counter + 1
    i = i - 1

print(counter)

