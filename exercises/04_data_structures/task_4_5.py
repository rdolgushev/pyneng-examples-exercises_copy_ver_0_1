# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans_1 = command1.split()
vlans_2 = command2.split()

vlans_1_list = vlans_1[4].split(',')
vlans_2_list = vlans_2[4].split(',')

vlans_1_set = set(vlans_1_list)
vlans_2_set = set(vlans_2_list)

vlans_all = list(vlans_1_set.intersection(vlans_2_set))

print(sorted(vlans_all))