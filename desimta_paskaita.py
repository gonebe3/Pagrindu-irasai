# def spausdinti_teksta(tekstas):
#     """
#     Funkcija spausdina teksta.
#     :param tekstas: Tekstas, kuris bus spausdinamas.
#     """
#     print('='*40)
#     print(tekstas)
#     print('='*40)
 
# spausdinti_teksta('Labas rytas!')
# spausdinti_teksta('Labas vakaras!')
# spausdinti_teksta('Labas naktis!')
 
 
# def pakelti_kvadrata(n): # n = 5
#     """
#     Funkcija pakelia skaičių kvadratu.
#     :param n: Skaičius, kurį reikia pakelti kvadratu.
#     :return: Pakeltas kvadratu skaičius.
#     """
#     return n ** 2
 
# pakelti_kvadrata(5) # vietoje funkcijos atsistoja 5^2 = 25
 
 
# 25
 
# def pasisveikinti(vardas, pavarde):
#     """
#     Funkcija pasisveikina su žmogumi.
 
#     :param vardas: Zmogaus vardas su kuriuo sveikinames.
 
#     :param pavarde: Pavardė.
 
#     """
#     print(f'Labas, {vardas} {pavarde}!')
#     # jeigu nera returno galima isvaizduoti, kad programa automatiskai padaro
#     # return None
 
# pasisveikinti('Jonas', 'Jonaitis')
# None # jis dar ivyko print savo viduje
# pasisveikinti('Petras', 'Petraitis')
# pasisveikinti('Ona', 'Onaitė')
# pasisveikinti('Marytė', 'Marytė')
 
# value ir reference argumentai
 
 
 
# def spausdinti_teksta(tekstas):
#     print('='*40)
#     print(tekstas)
#     print('='*40)
 
# spausdinti_teksta("Tekstinis")
 
# def kvadratu(x): # x yra naujas lokalus (funkcijos ribose) kintamasis, kuris sukuriamas iskvieciant funkcija # kintamieji yra lokalus ir globalus
#     x = x ** 2
#     return x
 
# x = 5
# print(x)
# rezultatas = kvadratu(x)
# print(x)
 
# print(rezultatas) # 25
 
 
# def kvadratu(sk): # sk = 5
#     sk = sk ** 2
#     return sk
 
# x = 5
# print(x)
# rezultatas = kvadratu(x)
 
# print(x)
 
# print(rezultatas) # 25
 
 
 
# def grazink_skaiciu():
#     return 5,9,4
 
# print(grazink_skaiciu())
 
 
# def pakelti_sarasa_laipsniu(sarasas, laipsnis):
#     """
#     Funkcija pakelia kiekvieną skaičių sąraše kvadratu.
 
#     :param sarasas: Sąrašas, kurį reikia pakelti kvadratu.
#     :return: Naujas sąrašas su pakeltais kvadratu skaičiais.
#     """
#     index = 0
#     while index < len(sarasas):
#         sarasas[index] = sarasas[index] ** laipsnis # sarasas[0] = sarasas[0] ** 2 | sarasas[1] = sarasas[1] ** 2 | sarasas[2] = sarasas[2] ** 2
#         index += 1
 
 
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# pakelti_sarasa_laipsniu(my_list,3)
# print(my_list)
 
 
# def kvadratu(x): # x = 5
#     """
#     Funkcija pakelia skaičių kvadratu.
 
#     :param x: Skaičius, kurį reikia pakelti kvadratu.
#     :return: Pakeltas kvadratu skaičius.
#     """
#     return x ** 2
 
# sk = 5
# print(kvadratu(sk)) # 25
# print(sk)
 
# def prideti_elementa(sarasas): # sarasas = 0x7f8c4c0b3d90
#     sarasas.append(5)
#     return sarasas
 
# my_list = [1, 2, 3, 4] # my_list = 0x7f8c4c0b3d90
# print(my_list) # [1, 2, 3, 4]
# prideti_elementa(my_list) # [1, 2, 3, 4, 5]
# print(my_list) # [1, 2, 3, 4, 5]
 