import requests
from time import sleep

url1 = 'http://52c28bb4-6891-4164-8c3c-1da41bb78657.node4.buuoj.cn:81'  # url为被扫描地址，后不加‘/’

# 常见的网站源码备份文件名  同目录下创建List.txt 如web,website,backup,back,www,wwwroot,temp等
# with open('List1.txt', 'r') as f:
#     list1 = f.read().splitlines()
list1=['web', 'website', 'backup', 'back', 'www', 'wwwroot', 'temp', 'robots', 'index.php', '.index.php','site']

# 常见的网站源码备份文件后缀
list2 = ['tar', 'tar.gz', 'zip', 'rar', '7-zip', '7z', 'txt', 'bak', 'swp','bzr','hg','idea','snv','git']
for i in list1:

    for j in list2:
        back = str(i) + '.' + str(j)
        url = str(url1) + '/' + back
        if(requests.get(url).status_code==200):
            print(back + '    ', end='')
            print(requests.get(url).status_code)

        # 结果返回的是状态码，如果状态码为200则存在
    sleep(0.5);
