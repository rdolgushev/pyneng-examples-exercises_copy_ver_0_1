# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac_list = mac.split(':')

mac_bin_a = bin(int((mac_list[0]), 16))[2:]
mac_bin_b = bin(int((mac_list[1]), 16))[2:]
mac_bin_c = bin(int((mac_list[2]), 16))[2:]

print(mac_bin_a + mac_bin_b + mac_bin_c)