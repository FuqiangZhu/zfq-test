# 装饰器
def school(func):
    def deco(name):
        print('---')
        func(name)
        print('===')
    print('deco', deco)
    return deco


@school
def student(name):
    print(name)
    print('zhangsan')


# studen1 = school(student)
# studen2 = school(student)
# print(studen1)
# print(studen2)
# print(student)
student('lisi')
