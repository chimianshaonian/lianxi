class J:
    pass

class I(J):
    pass

class H(J):
    pass

class G(I):
    pass

class F(I):
    pass

class E(H):
    pass

class D(G):
    pass

class C(F):
    pass

class B(E):
    pass

class A(B, C, D):
    pass

"""
在调用时，A没有的属性，从其他父类里寻找
找的循序为：BEHCFDGIJ
"""

# 查看A类的继承顺序，用mro
print(A.mro())
print(A.__mro__)