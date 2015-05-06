# -*- coding:utf-8 -*-
__author__ = 'jinjuoh'

member = ["colrodia", "jinju7373", "gpwjd0818"]
print(member[0])
print(member[1])
print(member[2])

print("--")

def get_members():
    return ["colrodia", "jinju7373", "gpwjd0818"]

members = get_members()

for member in members:
    print(member.capitalize())

print("--")

l = [1,2,3,4,5]
print(len(l))

li = ['a', 'b', 'c', 'd', 'e']
li.append('f')

print(li)

li.extend(['g','h'])

print(li)

li.insert(0, 'z')

print(li)

li.insert(2, 'B')

print(li)

li.pop(0)

print(li)

li.pop()

print(li)

li.sort()

print(li)

li.sort(reverse=True)

print(li)