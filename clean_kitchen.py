class Inner:
    def __init__(self):
        self.item = {}

    def additems(self, item):
        self.item[item.name] = item
        return 'Продукт добавлен'

    def getitems(self, name: str):
        items = self.item.values()

        for item in items:
            if item.name == name:
                thing = self.item[name]
                self.item.pop(name)
                return thing

        return None

    def __str__(self):
        return str(self.item)


class Product:
    def __init__(self, name):
        self.name = name
        self.state = 'Хороший'

    def identety(self):
        return '🍗'

    def __str__(self):
        return f'🍗 {self.name}:{self.state}'


class Refrigerator(Inner):
    def __init__(self):
        super().__init__()
        self.frig = Frig()

    def getitems(self, name: str):
        obj = super().getitems(name) or self.frig.getitems(name)

        #obj.pop(name)
        return obj

    def addFrigitems(self, item):
        self.frig.additems(item)
        return 'Продукт добавлен'

    def __str__(self):
        return str((self.item, self.frig.__str__()))


class Apple(Product):
    pass


class Cherry(Product):
    pass


class Mango(Product):
    pass


class Chicken(Product):
    pass


class Pork(Product):
    pass


class Frig(Inner):
    def __init__(self):
        super().__init__()



class Shelve(Refrigerator):
    pass


class Tomat(Product):
    pass


class Locker(Inner):
    pass


class Stove:
    def __init__(self):
        pass

    def cook(self, meal):
        meal.state = 'Жаренный'
        return meal


