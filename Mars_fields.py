from clean_kitchen import *

mr_freeze = Refrigerator()
mr_box = Locker()
steam_machine = Stove()


pork = Pork('Свинина')

print(pork)
print(mr_freeze.addFrigitems(pork))
print(steam_machine.cook(mr_freeze.getitems('Свинина')))
print(mr_freeze.additems(pork))
