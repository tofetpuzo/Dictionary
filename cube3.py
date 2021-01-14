x = int(input("what number do you want the square root of: "))

epsilon = 0.01
numGuesses = 0
low = x/3
high = max(1, x)
ans = (high+ low) / 3.0
while abs(ans**3 - x) >= epsilon:
    print('low = ', low, 'high = ', high, 'ans = ', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans 
    else:
        high = ans
    ans = (high + low)/ 3.0
    
print('numGueses =', numGuesses)
print(ans, 'is close to cube-root of ', x)


