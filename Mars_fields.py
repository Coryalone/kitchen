from clean_kitchen import *

mr_freeze = Refrigerator()
mr_box = Locker()
steam_machine = Stove()


pork = Pork('Свинина')
apple = Apple('Яблоко')

#print(mr_freeze.item['Свинина'])
#print(pork)
print(mr_freeze.addFrigitems(pork))
print(mr_freeze.additems(apple))
print(mr_freeze.frig.item['Свинина'])
print()
print(mr_freeze.additems(steam_machine.cook(mr_freeze.getitems('Свинина'))))
#print(mr_freeze.getitems('Свинина'))
print(mr_freeze.item['Свинина'])
