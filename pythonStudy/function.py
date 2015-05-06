# -*- coding:utf-8 -*-
__author__ = 'jinjuoh'


def numbering():
    i = 0
    while i < 10:
        print(i)
        i+=1


numbering()


print("--")

def get_member1():
    return "colrodia"

def get_member2():
    return "jinju7373"

print(get_member1())
print(get_member2())


print("--")

def get_argument(arg):
    return arg

print(get_argument(1))
print(get_argument(2))

print("--")

def get_arguments(arg1, arg2):
    return arg1 + arg2

print(get_arguments(10,20))
print(get_arguments(20,30))

print("--")

def get_arg_default(arg=100):
    return arg

print(get_arg_default(1))
print(get_arg_default())