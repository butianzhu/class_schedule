#类的使用
# class Song(object):
#
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
#  happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around teh family",
#                         "With pockets full of shells"])
#
# happy_bday.sing_me_a_song()
#
# bulls_on_parade.sing_me_a_song()


#隐式继承
# class Parent(object):
#
#     def implicit(self):
#         print("PARENT implicit()")
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()


#显示覆盖
# class Parent(object):
#
#     def override(self):
#         print("PARENT override()")
#
# class Child(object):
#
#     def override(self):
#         print("CHILD override()")
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()


#运行前后替换
# class Parent(object):
#
#     def override(self):
#         print("PARENT override()")
#
# class Child(object):
#
#     def override(self):
#         print("CHILD,BEFOR PARENT override()")
#         super(Child , self).override()
#         print("CHILD,AFTER PARENT override()")
#
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()


#组合
class Other(object):

    def Override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD,before other altered()")
        self.other.altered()
        print("CHILD,after other altered()")

son = Child()

son.implicit()
son.override()
son.altered()
