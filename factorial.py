#calculate factorial
n=int(input("Enter n \n"))
fact=1
for i in range(1,n+1) :
    fact=fact*i

print(f"Factorial is {fact}")