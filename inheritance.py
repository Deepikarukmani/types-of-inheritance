#inheritance
class dad():
    def phone(self):
        print("dad's phone")

class mom():
    def apple_watch(self):
        print("mom's apple watch")

class daughter(dad,mom):
    def laptop(self):
        print("favorite laptop")

titi=daughter()
titi.phone()
titi.apple_watch()


#multilevel inheritance:

class grandpa():
    def telephone(self):
        print("grandpa's telephone")

class dad(grandpa):
    def money(self):
        print("dad's money")

class daughter(dad,grandpa):
    def laptop(self):
        print("her favorite laptop")

deepika=daughter()
deepika.money()
deepika.telephone()
gowtham = dad()
gowtham.telephone()

#Hierarchical inheritance:

class dad():
    def money(self):
        print("dad's money")

class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

sakthi=son1()
sakthi.money()
jeeva=son2()
jeeva.money()
abhi=son3()
abhi.money()

#hybrid inheritance
class dad():
    def money(self):
        print("dad's money")

class land():
    def patta(self):
        print("land patta")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

sinchan = son1()
sinchan.money()
sinchan.patta()
