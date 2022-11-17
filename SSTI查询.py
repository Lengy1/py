import time

ktime = time.time()


def ssti():
    a = input("输入完整的字符串：")
    global aa
    aa = a.split(",")
    print("-----------------已经处理好了,可以进行查询了-----------------")
    j = chaxuen()


def chaxuen():
    global line
    try:
        c = input("输入要查询的字符串：")
        for i, line in enumerate(aa):
            if c in line:
                print("\n该字符串的位置为: " + str(i), line, '\n--------------查询成功-------------')
        if "" in line:
            print("\n没有查询到该字符串\n")

    except Exception as e:
        print(e)


if __name__ == "__main__":

    d = 0
    while d == 0:
        print("<<< 是否开始查询 请输入 yes/no >>>")
        user = input(': ')

        while (user != 'yes' and user != 'no'):
            print("输入错误!请重新输入:")
            user = input("：")

        if user == "yes":
            e = ssti()

        if user == "no":
            print("欢迎下次光临")
            break

wtime = time.time()
ss = repr(wtime - ktime)[0:6]
print("本次使用时间:" + str(ss) + "秒")