def factorial(n) :
    product=1
    while n>0:
        product=product*n
        n=n-1
    return product

n=input("Please input x:")
product=factorial(int(n))
print(product)

str=list(str(product))
print(str)
num=str.count("0")
print(num)
