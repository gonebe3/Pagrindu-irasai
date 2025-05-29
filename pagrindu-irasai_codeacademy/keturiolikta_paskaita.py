# class Dog():
#     def __init__(self):
#         self.__kojos = 4 # __ pries kintamaji reiskia, kad jis yra privatus (pasiekiamas tik klases viduje)
 
#     def keisti_kojas(self, kojos):
#         if kojos >= 0 and kojos < 6:
#             self.kojos = kojos
 
 
#     def __vidinis(self):
#         print("As vidinis")
 
#     def _spausdinti_kojas(self):
#         print(self.kojos)
#         self.__vidinis()
 
# suo1 = Dog()
# suo2 = Dog()
 
# # print(suo1.__kojos)
# # suo1.__kojos = 3
# # print(suo1.kojos)
# suo1.keisti_kojas(3)
# suo1._spausdinti_kojas()
# # suo1.__vidinis()
# # print(suo2.kojos)
 
# # suo1.naujas = 9 # retai naudojama ganetinai unikali python savybe
# # print(suo1.naujas)
 
# _________________________________________________
# REPR PANAUDOJIMAS 


# class Dog():
#     def __init__(self):
#         self.__kojos = 4 # __ pries kintamaji reiskia, kad jis yra privatus (pasiekiamas tik klases viduje)
 
#     def keisti_kojas(self, kojos):
#         if kojos >= 0 and kojos < 6:
#             self.__kojos = kojos
 
 
#     def _spausdinti_kojas(self):
#         print(self.__kojos)
#     def __str__(self): # str skirtas atvaizduoti daugiau, kai mus domina konkretus objektas tarsi duok informacija apie objekta
#         return f" str metodas {self.__kojos}"
#     def __repr__(self): # repr skirtas atvaizduoti "Bare minimum", kai mus domina tik supratimas apie kokia objekta eina kalba, bet detales nedomina. Nuo zodzio Represent.
#         return f" repr metodas {self.__kojos}"
 
# suo1 = Dog()
# suo2 = Dog()
 
# # print(suo1.__kojos)
# # suo1.__kojos = 3
# # print(suo1.kojos)
# suo1.keisti_kojas(3)
# suo1._spausdinti_kojas()
# # suo1.__vidinis()
# # print(suo2.kojos)
 
# # suo1.naujas = 9 # retai naudojama ganetinai unikali python savybe
# # print(suo1.naujas)
 
 
# suo1.begti() # printina as begu
# suo1.begti() # pasitikrina kiek turi koju ir tada printina as begu su tam tikru kiekiu koju
# stringas = str("Blablabla")
# stringas.
 
# sunys = [suo1,suo2]
 
# # print(sunys) # kai printinam objektu sarasa naudojamas __repr__
 
# for suo in sunys:
#     print(suo) # kai printinam viena objekta, su print, tuomet naudojamas __str__
 
# class Cat():
#     pass
 
# sunys.append(Cat())
 
# for suo in sunys:
#     if type(suo) is Dog:
#         suo._spausdinti_kojas()





