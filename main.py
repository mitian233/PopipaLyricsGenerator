import random
from dictionary import meishi
from dictionary import doushi
from dictionary import jyoushi
from dictionary import fukushi

a = random.randint(1, 13)
b = random.randint(1, 2)
c = random.randint(0, 1)
d = random.randint(1, 3)
moresentences1 = random.randint(0, 1)

if c == 0:
    result1 = (meishi[a] + jyoushi[b] + doushi[d])
else:
    result1 = (meishi[a] + jyoushi[b] + fukushi[c] + 'に' + doushi[d])

if moresentences1 == 0:
    print(result1 + '。')
else:
    a = random.randint(1, 13)
    b = random.randint(1, 2)
    c = random.randint(0, 1)
    d = random.randint(1, 3)
    if c == 0:
        result2 = (meishi[a] + jyoushi[b] + doushi[d])
    else:
        result2 = (meishi[a] + jyoushi[b] + fukushi[c] + 'に' + doushi[d])
    print(result1 + '、' + result2 + '。')
