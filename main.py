import time


def foo(x, y):
    print("calculating....")
    x = x * 2
    y = y * 2
    time.sleep(1)
    return y * x


if __name__ == '__main__':
    print("start app")
    print(foo(1, 2))
    print("stop app")
