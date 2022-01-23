#Factorial digit sum
ans = 1
for i in range(1,101):
    ans = ans * i
d = [int(dig) for dig in str(ans)]
total = sum(d)
print(total)