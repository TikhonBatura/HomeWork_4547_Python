def fact (n):
    
    if n == 0:
        return 1
    
    return n*fact(n-1)

def trig_num (n):
    if n == 1:
        return 1
    
    return n + trig_num (n-1)
    
N = int(input("Please input some number: "))

print(fact(N))
print(trig_num(N))