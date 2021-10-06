# q = [1,2,4]
# w = (1,2,4)
#
# print(q.__sizeof__())
# print(w.__sizeof__())

try:
    q = 10 / 1
except ZeroDivisionError as e:
    print(e)
else:
    print('qqqq')
finally:
    print('finally')


