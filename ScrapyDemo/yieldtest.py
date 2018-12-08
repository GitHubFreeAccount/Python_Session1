# -*- coding: utf-8 -*-
# dict 字典 相对于其他语音的map表


from inspect import isgeneratorfunction


# 无返回值 直接在用print打印
def fab(max):
    num, a, b = 0, 0, 1
    while num < max:
        print(b)
        a, b = b, a + b
        num = num + 1


def fab1(max):
    num, a, b = 0, 0, 1
    array = []
    while num < max:
        array.append(b)
        a, b = b, a + b
        num = num + 1
    return array


'''
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator 生成器
 调用 fabyield(5) 不会执行 fabyield 函数，而是返回一个 iterable 对象！在 for 循环执行时，
 每次循环都会执行 fabyield 函数内部的代码，
  执行到 yield b 时，fabyield 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中
  断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，
 比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
'''


def fabyield(max):
    num, a, b = 0, 0, 1
    while num < max:
        yield b
        a, b = b, a + b
        num = num + 1


if __name__ == '__main__':
    fab(5)
    print "------------------"
    for n in fab1(5):
        print n
    print "------------------"
    for n in fabyield(5):
        print n

    print isgeneratorfunction(fab)
    print isgeneratorfunction(fabyield)
    # 分割字符串为字符串数组
    print "i love you".split()

    urls = 'http://ww3.sinaimg.cn/mw600/0073tLPGgy1fxidfpbgkmj30oo0zkdnn.jpg'
    print urls.rsplit('/')[-1]
