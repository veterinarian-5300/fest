n=int(input("Enter a number whose divisors you wanna know "))
print("The list of divisors in increasing order are")

for i in range(0,n):
    if n%i==0:
        print(i,' ',end='')
        
