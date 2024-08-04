def test1(a,b):
    print(a * b)

def test2(a,b):
    print(a - b)

# 调试代码，有main后，调用该模块时，就不在执行调试代码
if __name__ == '__main__':

    test1(5,10)


test1(2,3)