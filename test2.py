from clean_kitchen import *

mr_freeze = Refrigerator()
mr_box = Locker()
steam_machine = Stove()

apple = Apple('Яблоко')
mango = Mango('Манго')
chicken = Chicken('Курица')
tomat = Tomat('Томат')
pork = Pork('Свинина')

print(mr_freeze.additems(apple))
print(mr_freeze.additems(tomat))
print(mr_freeze.additems(pork))
print(mr_freeze.getitems('Яблоко'))
print(mr_freeze.getitems('Свинина'))

print(mr_box.additems(tomat))
print(mr_box.getitems('Томат'))

print(steam_machine.cook(pork))