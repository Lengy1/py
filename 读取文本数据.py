import base64
f = open("test.txt", "rb")
data = f.read()


f1= open("res.cab", "wb")



# t=0
# for i in data[::2]:
#   s=int((data[t:t+2]),16)
#   print(hex(s^a),end="")
#   t+=28

#以两字节为组读取 分别异或
#data=data.replace('\n', '')
#data=data.replace('\r', '')
#fp=open("output.txt","a+")
#for t in range(0,len(data),2):
  #s=int(data[t:t+2],16)
  #print('%02x'%(s^a), file=fp,end=" ")

