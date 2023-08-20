import os
os.system('cls')
import numpy as np

def _break():
    print()
    print('____________________________________')
    print()
    

lst = [2,4,3,1]

array = np.array(lst)

print(lst)
print(type(lst))
print(array)
print(type(array))

_break()

lst = [[1,2,3],[4,5,6],[7,8,9]]
print(lst)
print()
array = np.array(lst)
print(array)

_break()

# لیست یک بعدی
one_dimensional = [1, 2, 3]
print("Number of dimensions:", len(one_dimensional))
print("Size of each dimension:", len(one_dimensional))
print()
# لیست دو بعدی
two_dimensional = [[1, 2, 3], [4, 5, 6]]
print("Number of dimensions:", len(two_dimensional))
print("Size of first dimension:", len(two_dimensional))
print("Size of second dimension:", len(two_dimensional[0]))
print()

# لیست سه بعدی
three_dimensional = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("Number of dimensions:", len(three_dimensional))
print("Size of first dimension:", len(three_dimensional))
print("Size of second dimension:", len(three_dimensional[0]))
print("Size of third dimension:", (three_dimensional[0][0][1]))

_break()

lst = [0 for i in range(10)]
print(lst)


#است float به طور پیش فرض 
# array = np.zeros(10)
# array = np.zeros(10,int)
# array nD
# array = np.zeros((3,3,2),int)
# array = np.ones((2,1),int)
# میتونی هر عددی رو استفاده کنی
array = np.full((2,3,4),5,int)
x = array.ndim
print(array)
print(x)

_break()

# اعداد تصادفی در np
# اعداد بین 0 و 1
print(np.random.random(5))
# اعداد بین 0و10
print(np.random.random(5)*10)
print(np.array(np.random.random(5)*1000,int))

_break()

# reshape میاد و شکل آرایه رو تغییر به بعد های دیگر میکنه 
# ولی لیست اصلی رو تغییر نمیدهد

# 1d
lst = [1,2,3,4,5,6,7,8,9,10]

array = np.array(lst)
# print(array)
# (ستون و سطر)
# 2d
print(array.reshape((5,2)))
print(array) 
# بریز array اگر میخوای لیست آرایه هم تغییری بکنه باید داخل خود متغییر 
#None استفاده کن ولی چیزی بر نمیگردونه در اصل به صورت.resize   یا از 
print()
print(array.resize((5,2)))
print(array) 

#استفاده کنی reshape اگر میخوای به حالت اول ببری باید از 
# -1 میاد و یک بعدی میکنه
print(array.reshape(-1))
print(array)

_break()
#  یک بازه بین 0 تا 20 داریم میخوام اون این وسط 5تا نقطه بزاریم و فاصله بین اعداد یکی باشد
# (تعداد نقطه و پایان اعداد و شروع اعداد)
print(np.array(np.linspace(1,10,4),int))

_break()
# اگر بخوای جا سطر و ستون رو عوض کنی 
# در اصل روی قطر اصلی بر میگرونیم   

array = np.array([[1,2],[3,4],[5,6]])
print(array.transpose())

_break()

# arange یک رنج از اعداد میگیره 

print(np.arange(0, 11 , 2))

