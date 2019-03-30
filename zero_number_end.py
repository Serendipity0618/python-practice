def factorial(n):
    product = 1
    while n > 0:
        product = product * n
        n = n - 1
    return product


n = input("Please input x:")
product = factorial(int(n))
print(product)

counter = 0
while product % 10 == 0:
    product = (product // 10)
    counter = counter + 1

print(counter)
