'''練習模擬一個冰淇淋小店'''


class IceCreamStand():
    def __init__(self, stand_name, position, *flavors):
        self.stand_name = stand_name
        self.position = position
        self.flavors = flavors

    def sell(self):
        s_ice = ''
        for ss in self.flavors:
            s_ice = s_ice + ss + ','
        print('坐落在' + self.position + '的' + self.stand_name + '冰淇淋店賣' + s_ice)


# stand = IceCreamStand('JerryPg', 'fololusa', '1', '2', '3', '4')
# stand.sell()

from collections import OrderedDict
from random import randint

class Die():
    '''擲骰子遊戲'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print('投擲骰子：'+str(randint(1,self.sides)))

'''
i=0
while i<10:
    die=Die(20)
    die.roll_die()
    i+=1
'''
