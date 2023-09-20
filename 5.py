k = 0
for n in range(1, 2000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '00'
    else:
        b += '10'
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    r = int(b, 2)
    if (k >= 130) and (k <= 350):
        k += 1
print(k)
