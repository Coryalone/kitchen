from kitchen import *


mr_freeze = Refrigerator(15)
mr_box = Locker()

apple = Apple()
mango = Mango()
chicken = Chicken()
tomat = Tomat('Томат')
print(mr_freeze.additems(apple, 5))
print(mr_freeze.additems(tomat, 5))
mr_freeze.frig.additems(chicken, 5)
print(mr_freeze.getitems('apple', 4))

print(mr_box.additems(tomat))
print(mr_box.getitems('Томат'))
