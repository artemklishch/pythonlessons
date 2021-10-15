import libs
import os
# import random as r
# import random
# from random import randint, shuffle
from random import *

print(os.getcwdb())
# print(r.randint(1, 100))
# print(random.randint(1, 100))
print(randint(1, 100))

l1 = [1, 2, 3, 4, 5]
shuffle(l1)
print(l1)

print(__name__)
print(libs.get_count("Hello world", "l"))
print(libs.get_len("helo"))

f1 = libs.get_count
print(f1("Hello world", "o"))
