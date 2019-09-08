class Person:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)
    def __del__(s
        print("%s 走了" %self.name)
tom = Person('Tom')
del tom