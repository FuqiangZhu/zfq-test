# # # # # # # # # # #
# # # # # # # # # # def fib(max1):
# # # # # # # # # #     n, a, b = 0, 0, 1
# # # # # # # # # #     while n < max1:
# # # # # # # # # #         print(b)
# # # # # # # # # #         d = yield b
# # # # # # # # # #         print('d', d)
# # # # # # # # # #         a, b = b, a + b
# # # # # # # # # #         n += 1
# # # # # # # # # #     return '测试呢'
# # # # # # # # # #
# # # # # # # # # # # print('--==--')
# # # # # # # # # # # # cf = fib(10)
# # # # # # # # # # # cf = [1, 3, 5]
# # # # # # # # # # # print(cf)
# # # # # # # # # # # print(range(10))
# # # # # # # # # # # cmm = map(lambda n:n*n, cf)
# # # # # # # # # # # print(type(cmm))
# # # # # # # # # # # for i in cmm:
# # # # # # # # # # #     print(i)
# # # # # # # # # # # c = fib(10)
# # # # # # # # # # # # for i in c:
# # # # # # # # # # # #     print('i', i)
# # # # # # # # # # # next(c)
# # # # # # # # # # # print('---')
# # # # # # # # # # # c.send(12)
# # # # # # # # # # # print('---')
# # # # # # # # # # # next(c)
# # # # # # # # # # # print('---')
# # # # # # # # # # # # next(c)
# # # # # # # # # # # # next(c)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # # def consumer(name):
# # # # # # # # # # #     print('%s 准备好了' % name)
# # # # # # # # # # #     while True:
# # # # # # # # # # #         bao = yield
# # # # # # # # # # #         print('%s来了，%s开始吃了' % (bao, name))
# # # # # # # # # # #
# # # # # # # # # # # c = consumer('张三')
# # # # # # # # # # # c.__next__()
# # # # # # # # # # # print('---')
# # # # # # # # # # # c.send('w')
# # # # # # # # # # # print('---')
# # # # # # # # # # # c.__next__()
# # # # # # # # # # # print('---')
# # # # # # # # # # # c.__next__()
# # # # # # # # # # # print('---')
# # # # # # # # # #
# # # # # # # # # # from collections import Iterable
# # # # # # # # # # from collections import Iterator
# # # # # # # # # #
# # # # # # # # # # # print(isinstance([], Iterable))
# # # # # # # # # # # s = set([12, 2])
# # # # # # # # # # # print(isinstance(s, Iterator))
# # # # # # # # # # # print(s)
# # # # # # # # # # # print(isinstance(iter([]), Iterator))
# # # # # # # # # # # print(isinstance(iter('abc'), Iterator))
# # # # # # # # # # # ss = iter('abc')
# # # # # # # # # # # print(ss.__next__())
# # # # # # # # # # #
# # # # # # # # # # # print('--=--')
# # # # # # # # # #
# # # # # # # # # # code = '''
# # # # # # # # # # def code():
# # # # # # # # # #     print('123sd')
# # # # # # # # # #     return '22'
# # # # # # # # # #
# # # # # # # # # # code()
# # # # # # # # # # '''
# # # # # # # # # # # cc = compile(code, '', 'exec')
# # # # # # # # # # # print(exec(code))
# # # # # # # # # # # exec(code)
# # # # # # # # # #
# # # # # # # # # # a = 1
# # # # # # # # # # # print(dir(a))
# # # # # # # # # # # print(divmod(4, 3))
# # # # # # # # # # # print(eval(2))
# # # # # # # # # # # eval(code)
# # # # # # # # # # # print(eval('a + 2'))
# # # # # # # # # # # print('==-==')
# # # # # # # # # #
# # # # # # # # # # # x = lambda n: print(n)
# # # # # # # # # # # x(2)
# # # # # # # # # #
# # # # # # # # # # # print('---')
# # # # # # # # # # # cs = filter(lambda n: n > 5, range(10))
# # # # # # # # # # # for i in cs:
# # # # # # # # # # #     print(i)
# # # # # # # # # # # print(type(cs))
# # # # # # # # # #
# # # # # # # # # # # cm = map(lambda n:n*n, range(10))
# # # # # # # # # #
# # # # # # # # # # # print(type(cm))
# # # # # # # # # # # for i in cm:
# # # # # # # # # # #     print(i)
# # # # # # # # # # print('===')
# # # # # # # # # #
# # # # # # # # # # # print(bin(3))
# # # # # # # # # # # print(bool(1))
# # # # # # # # # # # print(bytes(1))
# # # # # # # # # # #
# # # # # # # # # # # print(chr(100))
# # # # # # # # # # # ccs = compile(code, '', 'ccc')
# # # # # # # # # # # exec(code)
# # # # # # # # # # # ac = complex(1, 2)
# # # # # # # # # # # print(ac)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # class Person:
# # # # # # # # # #     def __init__(self, name, age):
# # # # # # # # # #         print('name', name, 'age', age)
# # # # # # # # # #         self.name = name
# # # # # # # # # #         self.age = age
# # # # # # # # # #
# # # # # # # # # # person = Person('Tom', 12)
# # # # # # # # # # # print(dir(person))
# # # # # # # # # # # # delattr(person, 'age')
# # # # # # # # # # # print(divmod(1, 1))
# # # # # # # # # # #
# # # # # # # # # # # print('-----')
# # # # # # # # # # # print(float('2.3'))
# # # # # # # # # # # print(eval("{'ka':'2', 'dd':'2'}"))
# # # # # # # # # #
# # # # # # # # # # # from functools import reduce
# # # # # # # # # # # cc = reduce(lambda n,y:n+y, range(10))
# # # # # # # # # # # print(cc)#
# # # # # # # # # # # print(globals())
# # # # # # # # # # # ev = eval('[1, 2, 3]')
# # # # # # # # # # # print(type(repr('[1,d 2, 3]')))
# # # # # # # # # # print(vars(person))
# # # # # # # # # #
# # # # # # # # # # deco = __import__('deco')
# # # # # # # # # # # import deco
# # # # # # # # # # # __import__()
# # # # # # # # # #
# # # # # # # # # # deco.student('zhangdan')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Person(object):
# # # # # # # # #     def __init__(self, name):
# # # # # # # # #         self.name = name
# # # # # # # # #
# # # # # # # # #     def whoAmI(self):
# # # # # # # # #         print('i name is ', self.name)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Teacher(Person):
# # # # # # # # #     def __init__(self, name, course):
# # # # # # # # #         super(Teacher, self).__init__(name)
# # # # # # # # #         self.course = course
# # # # # # # # #
# # # # # # # # #     def tech(self):
# # # # # # # # #         print('i name is ', self.course)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Student(Teacher):
# # # # # # # # #     def __init__(self, name, score, course):
# # # # # # # # #         super(Student, self).__init__(name, score)
# # # # # # # # #         self.course = course
# # # # # # # # #
# # # # # # # # # s = Student('王同学', '80', 'shuxue')
# # # # # # # # #
# # # # # # # # # s.whoAmI()
# # # # # # # # # s.tech()
# # # # # # # #
# # # # # # # #
# # # # # # # # class A:
# # # # # # # #     def __init__(self):
# # # # # # # #         self.n = 'A'
# # # # # # # #
# # # # # # # #
# # # # # # # # class B(A):
# # # # # # # #     def __init__(self):
# # # # # # # #         super(B, self).__init__()
# # # # # # # #         # self.n = 'B'
# # # # # # # #     pass
# # # # # # # #
# # # # # # # #
# # # # # # # # class C(A):
# # # # # # # #     def __init__(self):
# # # # # # # #         super(C, self).__init__()
# # # # # # # #         self.n = 'C'
# # # # # # # #     # pass
# # # # # # # #
# # # # # # # #
# # # # # # # # class D(B, C):
# # # # # # # #     # def __init__(self):
# # # # # # # #     #     self.n = 'D'
# # # # # # # #     pass
# # # # # # # #
# # # # # # # #
# # # # # # # # obj = D()
# # # # # # # #
# # # # # # # # print(obj.n)
# # # # # # #
# # # # # # #
# # # # # # # class Dog(object):
# # # # # # #     def __init__(self):
# # # # # # #         print('--init--')
# # # # # # #
# # # # # # #     @staticmethod
# # # # # # #     def eating():
# # # # # # #         print('eating')
# # # # # # #
# # # # # # #
# # # # # # # d = Dog()
# # # # # # # d.eating()
# # # # # #
# # # # # #
# # # # # # class Dog(object):
# # # # # #     def __init__(self, name):
# # # # # #         self.name = name
# # # # # #         print('name', name)
# # # # # #     age = 10
# # # # # #
# # # # # #     @staticmethod
# # # # # #     def eating():
# # # # # #         print('eating')
# # # # # #
# # # # # #     @classmethod
# # # # # #     def run(cls):
# # # # # #         print(cls.age)
# # # # # #
# # # # # # d = Dog('jack')
# # # # # # d.eating()
# # # # # # Dog.run()
# # # # #
# # # # #
# # # # # class Dog(object):
# # # # #     def __init__(self, name):
# # # # #         print('init')
# # # # #         self.name = name
# # # # #
# # # # #     @property
# # # # #     def run(self):
# # # # #         print('run', self.name)
# # # # #         # yield
# # # # #         return None
# # # # #
# # # # #     # @run.setter
# # # # #     # def run(self, age):
# # # # #     #     print(self.name, age)
# # # # #
# # # # # d = Dog('mai')
# # # # # d.run
# # # # #
# # # # # # d.run = 12
# # # # #
# # # # # # d.run.__next__()
# # # #
# # # #
# # # # class Person(object):
# # # #     """
# # # #     描述信息
# # # #     """
# # # #
# # # #     def __init__(self, name):
# # # #         self.name = name
# # # #         print('init')
# # # #
# # # #     def run(self):
# # # #         print('run', self.name)
# # # #
# # # #     def __call__(self, *args, **kwargs):
# # # #         print('call')
# # # #
# # # # p = Person('张三')
# # # # # dir(p)
# # # # p.run()
# # # # print(p.__module__)
# # # # print(Person.__doc__)
# # # # p()
# # # # print(p.__dict__)
# # #
# # #
# # # def func():
# # #     print('funcc')
# # #
# # # Foo = type('Foo', (object,), {'func': func})
# # # f = Foo
# # # f.func()
# #
# #
# # # 单例设计模式
# # class Person(object):
# #     __isinstance = None
# #
# #     @staticmethod
# #     def singleton():
# #         if Person.__isinstance:
# #             return Person.__isinstance
# #         else:
# #             Person.__isinstance = Person()
# #             return Person.__isinstance
# #
# #
# # p = Person.singleton()
# # print(p)
# # p1 = Person.singleton()
# # print(p1)
#
#
# # 单例
# class Dog(object):
#     __isinstance = None
#
#     def __init__(self):
#         pass
#         # return self.__isinstance
#
#     @staticmethod
#     def singleton():
#         if Dog.__isinstance:
#             return Dog.__isinstance
#         else:
#             # Dog.__isinstance = Dog()
#             return Dog.__isinstance
#
# d = Dog.singleton()
# d1 = Dog.singleton()
# print(d)
# print(d1)
#
