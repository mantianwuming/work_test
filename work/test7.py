class A(object):
    i = '0'
class B(A):
    pass
class C(A):
    pass

B.i = '1'
A.i = '2'
print(A.i, B.i, C.i)