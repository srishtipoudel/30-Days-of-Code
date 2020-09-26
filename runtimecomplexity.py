# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True    
num_test_cases=int(input())
for i in range(num_test_cases):
    n=int(input())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
