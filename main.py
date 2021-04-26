import random
from dictionary import meishi
from dictionary import doushi
from dictionary import jyoushi
from dictionary import fukushi

a = random.randint(1, 13)
b = random.randint(1, 2)
c = random.randint(0, 1)
d = random.randint(1, 3)

print(meishi[a] + jyoushi[b] + fukushi[c] + doushi[d])
