# x = int(input("what number do you want the square root of: "))

# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1, x)
# ans = (high + low) / 2.0
# while abs(ans**2 - x) >= epsilon:
#     print('low = ', low, 'high = ', high, 'ans = ', ans)
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans 
#     else:
#         high = ans
#     ans = (high + low)/ 2.0
# print('numGueses =', numGuesses)
# print(ans, 'is close to square-root of ', x)
high = max(1, 25)
print(high)