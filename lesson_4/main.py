# cats = [('Мартин', 5, 'Алексей', 'Егоров'),
# #         ('Фродо', 3, "Анна", "Самохина"),
# #         ('Вася', 4, "Андрей', 'Белов"),
# #         ('Муся', 7, "Игорь", "Бероев"),
# #         ("Изольда", 2, "Игорь", "Бероев")]
# #
#
# owner = {}
# for i in cats:
#     nameage = i[0] + ', ' + str(i[1])
#     owner[i[2:]] = nameage
#     # owner.setdefault(i[2:],[]).append(owner)
#     if i[2:] in owner.keys():
#         owner[i[2:]]
#
#
#
#
# for i in owner.items():
#     print(i)
# my_dict = {}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
#
# biggest_dict(a=5, b=10, c=10)
# print(my_dict)

import random
class Voin:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


    def hit(self, v):
        v.health -= self.damage
        print(f'УДАР В {v.name} У НЕГО {v.name,v.health}хп')


anton = Voin("Anton",100, 30)
victor = Voin("VICTOR", 100, random.randint(30,50))


while anton.health > 0 and victor.health > 0:
    if random.randint(1,2) == 2:
        anton.hit(victor)


