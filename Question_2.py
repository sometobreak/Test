# Первая реализация 
# Плюсы: Простая и понятная реализация, контроль над структурой класса
# Минусы: Ручное управление указателями на элементы списка, более долгое выполнение операций
class ListFIFO:
    def __init__(self, size):
        self.size = size
        self.list = [None] * self.size
        self.first_item = 0
        self.last_item = 0
        
    def add_item(self, item):
        if len(self.list) < self.size:
            self.list[self.last_item] = item
            self.last_item += + 1
        else:
            print("List is full!")
        

    def delete_item(self):
        if len(self.list) > 0:
            item = self.list[self.first_item]
            self.list = self.list[1:] + [None]
            self.last_item -= 1
        else:
            print("List is empty!")
        return item

    def get_list(self):
        return self.list
        


from collections import deque

# Вторая реализация 
# Плюсы: Более оптимизированный, работает быстрее
# Минусы: Использование сторонней библиотеки, меньше контроля над структурой
class BufferFIFO:
    def __init__(self, size):
        self.size = size
        self.list = deque(maxlen=size)

    def add_item(self, item):
        if len(self.list) < self.size:
            self.list.append(item)
        else:
            print("Buffer is full!")

    def delete_item(self):
        if len(self.list) > 0:
            return self.list.popleft()
        else:
            print("Buffer is empty!")

    def get_list(self):
        return list(self.list)


print("ListFIFO working...")
array = BufferFIFO(3)
array.add_item(1)
print(array.get_list())
array.add_item(2)
print(array.get_list())
array.add_item(3)
print(array.get_list())
array.delete_item()
print(array.get_list())
array.delete_item()
print(array.get_list())
array.add_item(1)
array.add_item(2)
print(array.get_list())
array.delete_item()
print(array.get_list())
print(" ")
print("BufferFIFO working...")
buffer = BufferFIFO(3)
buffer.add_item(1)
print(buffer.get_list())
buffer.add_item(2)
print(buffer.get_list())
buffer.add_item(3)
print(buffer.get_list())
buffer.delete_item()
print(buffer.get_list())
buffer.delete_item()
print(buffer.get_list())
buffer.add_item(1)
buffer.add_item(2)
print(buffer.get_list())
buffer.delete_item()
print(buffer.get_list())
