#coding: utf-8

import hashlib
dic = '0123456789qazwsxedcrfvtgbyhnujmikolp'
for a in dic:
  for b in dic:
    for c in dic:
    		t = 'try'+a+'66'+b+c
    		md5 = hashlib.md5((t).encode()).hexdigest()

    		if md5== 'c905ab50c96685d90c49bb6422aad136':
    			print(t)
