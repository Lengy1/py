#!/usr/bin/env python
# -*- coding:utf-8 -*-
# python3
import zipfile
import string
import binascii

def CrackCrc(f, crc):  # 通过枚举的方法暴力验证CRC，前提是已知长度
    for i in dic:
        for j in dic:
            for k in dic:
                for h in dic:
                    s = i + j + k + h   # 长度为4的字符
                    if crc == (binascii.crc32(s.encode())):
                        f.write(s)  # 记录爆破内容
                        return

def CrackZip():
    f = open("./output.txt", "w")
    for i in range(2,9):    # 生成2-8这几个数字，对应part文件名
        file = "./Moment.zip"
        crc = zipfile.ZipFile(file, 'r').getinfo(f'part{i}.txt').CRC
        CrackCrc(f,crc)
        print('\r' + "loading：{:%}".format(float((i - 1) / 7)), end='')
    f.close()
    with open("./output.txt", "r+", encoding='utf-8') as fr:
        res = fr.read()
    return res

if __name__ == "__main__":
    dic = string.ascii_letters + string.digits + '-{' + '}' # 字典，大小写+数字+短横线+大括号（UUID格式的flag）
    print("\nCRC32begin")
    res = CrackZip()
    print("\nCRC32finished\n")
    print(res)