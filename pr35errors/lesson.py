print("hello")
# print(100/0)
# print(1 + "2")
# print(int("text"))

try:
    num = 100 / '2'
    # num = 100 / 0
# except ZeroDivisionError:
#     num = 0
# except TypeError:
#     num = 1
except Exception:
    num = None
else:
    print("else")
finally:
    print("finally")

print(num)
print("hi")

print('\n')
while True:
    try:
        num = int(input("Entere number: "))
        if num > 0:
            break
    except Exception:
        print("incorrect number")
