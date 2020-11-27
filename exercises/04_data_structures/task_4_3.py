# -*- coding: utf-8 -*-
"""
Задание 4.3

Получить из строки config такой список VLANов:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config_list = config.split()
vlan_list = config_list[4]
vlan_list_edited = vlan_list.split(',')

print(vlan_list_edited)