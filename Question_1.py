#Плюсы: Простой и понятный спобоб
def isEven(value):
    return value % 2 == 0

#Плюсы: Работает быстрее, чем взятие остатка от деления
def bIsEven(number):
    return number & 1 == 0

print(bIsEven(2))
print(bIsEven(400))
print(bIsEven(12312321538))
print(bIsEven(1425634265347546756754))
print(bIsEven(11111111111))
print(bIsEven(1231416753745741))
print(bIsEven(23543426456456455479))
