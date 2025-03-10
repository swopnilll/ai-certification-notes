def isPrime(num):
    
    if num <= 1:
        return False;
    
    divisible = 2;
    
    while divisible <= num // 2:
        if num % divisible == 0:
            return False
        
        divisible += 1;
        
    
    return True;

def fib(n):
    
    if n <= 0:
        return -1
    
    if n == 1:
        return 0
    
    if n == 2 or n == 3:
        return 1
    
    prev = 1
    curr = 1
    sum = 1
    
    for i in range(4, n + 1):        
        curr = sum 
        sum = prev + curr 
        prev = curr 
        
    return sum;
  
def check_balance(brackets):
    check = 0
    
    for bracket in brackets:
        if bracket == '[':
            check += 1
        
        elif bracket == ']':
            check -= 1
        
        if check < 0:
            return False
    
    return check == 0
        
        
a = 10
b = 15


        
        
        
    
    
    

