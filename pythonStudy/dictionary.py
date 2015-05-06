# -*- coding:utf-8 -*-
__author__ = 'jinjuoh'


grade = {"colrodia":10, "jinju7373":6, "gpwjd0818":80}

print(grade)

grades = {}
grades["colrodia"] = 10
grades["jinju7373"] = 6
grades["gpwjd0818"] = 80

print(grades["colrodia"])

for key in grades:
    print("key : %s \t value : %s") % (key, grades[key])