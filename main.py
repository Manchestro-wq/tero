a = int(input('веди число:'))
i = 0
while a != 0:
    i = max(i, a)
    a = int(input('веди число:'))
print(i)