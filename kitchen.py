class Refrigerator:
    def __init__(self, capacity):
        self.item = {}
        self.count = {}
        self.capacity = capacity
        self.frig = Frig(10)

    def additems(self, item, count: int):
        if sum(self.count.values()) < self.capacity and (sum(self.count.values()) + count) <= self.capacity:
            self.item[item.name] = item
            if self.count.get(item.name) is None:
                self.count[item.name] = 0
                self.count[item.name] += count

            else:
                self.count[item.name] += count
            return 'Продукт добавлен'
        return 'перебор братиш'

    def getitems(self, name: str, count: int):
        items = self.item.values()
        frig_items = self.frig.item.values()
        print(frig_items)
        for item in items:
            if item.name == name:
                if (self.count[item.name] - count) >= 0:
                    self.count[item.name] -= count
                    thing = self.item[name]
                    return thing

        for item in frig_items:
            if item.name == name:
                if (self.frig.count[item.name] - count) >= 0:
                    self.frig.count[item.name] -= count
                    return f'Продукт выдан, продукта {self.frig.item[item.name]} осталось  {self.frig.count[item.name]}'
        return 'Холодильник пуст'


class Apple:
    def __init__(self):
        self.name = 'apple'

    def identety(self):
        return '🍎'

    def __str__(self):
        return '🍎'


class Cherry:
    def __init__(self):
        self.name = 'cherry'

    def identety(self):
        return '🍒'

    def __str__(self):
        return self.name


class Mango:
    def __init__(self):
        self.name = 'mango'

    def identety(self):
        return '🥭'

    def __str__(self):
        return self.name


class Chicken:
    def __init__(self):
        self.name = 'chicken'

    def identety(self):
        return '🍗'

    def __str__(self):
        return self.name


class Frig:
    def __init__(self, capacity):
        self.item = {}
        self.count = {}
        self.capacity = capacity

    def additems(self, item, count: int):
        #print('Продукт добавлен')
        if sum(self.count.values()) < self.capacity and (sum(self.count.values()) + count) <= self.capacity:
            self.item[item.name] = item
            if self.count.get(item.name) is None:
                self.count[item.name] = 0
                self.count[item.name] += count

            else:
                self.count[item.name] += count
            print('Продукт добавлен')
            return 'Продукт добавлен'
        print('ВНИМАНИЕ перебор братиш')
        return 'перебор братиш'

    def getitems(self, name: str, count: int):
        items = self.item.values()
        for item in items:
            if item.name == name:
                if (self.count[item.name] - count) >= 0:
                    self.count[item.name] -= count
                    return f'Продукт выдан, продукта {self.item[item.name]} осталось  {self.count[item.name]}'
        return 'Морозильник пуст'


class Shelve:
    def __init__(self, capacity):
        self.item = {}
        self.count = {}
        self.capacity = capacity

    def additems(self, item, count: int):
        if sum(self.count.values()) < self.capacity and (sum(self.count.values()) + count) <= self.capacity:
            self.item[item.name] = item
            if self.count.get(item.name) is None:
                self.count[item.name] = 0
                self.count[item.name] += count

            else:
                self.count[item.name] += count
            return 'Продукт добавлен'
        return 'перебор братиш'

    def getitems(self, name: str, count: int):
        items = self.item.values()
        for item in items:
            if item.name == name:
                if (self.count[item.name] - count) >= 0:
                    self.count[item.name] -= count
                    return f'Продукт выдан, продукта {self.item[item.name]} осталось  {self.count[item.name]}'
        return 'Полка пуста'


class Product:
    def __init__(self, name):
        self.name = name

    def identety(self):
        return '🍗'

    def __str__(self):
        return self.name


class Tomat(Product):
    pass


class Inner:
    def __init__(self):
        self.item = {}
        self.frig = Frig(10)

    def additems(self, item):
        self.item[item.name] = item
        return 'Продукт добавлен'

    def getitems(self, name: str):
        items = self.item.values()
        frig_items = self.frig.item.values()
        for item in items:
            if item.name == name:
                thing = self.item[name]
                return thing

        for item in frig_items:
            if item.name == name:
                thing = self.frig.item[name]
                return thing
        return 'Холодильник пуст'


class Locker(Inner):
    pass






'''
refrigerator = Refrigerator(10)
cherry = Cherry()
apple = Apple()
chicken = Chicken()
'''

'''
refrigerator.additems(cherry, 5)
print(refrigerator.additems(apple, 5))
#print(refrigerator.additems(apple, 5))


print(refrigerator.item)

print(refrigerator.getitems('apple', 3))
print('------------------')
print(refrigerator.count)
print(refrigerator.frig.additems(chicken, 5))
print(refrigerator.frig.getitems('chicken', 3))
'''

# сд
