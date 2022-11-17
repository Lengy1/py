import zipfile
zip_src='zip解压/Continue.zip'

# 基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
# mode：可选 r,w,a 代表不同的打开文件的方式；r 只读；w 重写；a 添加
# compression：指出这个 zipfile 用什么压缩方法，默认是 ZIP_STORED，另一种选择是 ZIP_DEFLATED；
# allowZip64：bool型变量，当设置为True时可以创建大于 2G 的 zip 文件，默认值 True；

# zip_file = zipfile.ZipFile(path)
# zip_list = zip_file.namelist()  # 得到压缩包里所有文件
#
# for f in zip_list:
#     zip_file.extract(f, folder_abs)  # 循环解压文件到指定目录
#
# zip_file.close()  # 关闭文件，必须有，释放内存


# zipfile.is_zipfile('xxx.zip') # 判断文件是否是个有效的zipfile
# zipfile.namelist('xxx.zip') # 列表，存储zip文件中所有子文件的path（相对于zip文件包而言的）
# zipfile.infolist('xxx.zip') # 列表，存储每个zip文件中子文件的ZipInfo对象
# zipfile.printdir() # 打印输出zip文件的目录结构，包括每个文件的path，修改时间和大小
# zipfile.open(name[,mode[,pwd]]) # 获取一个子文件的文件对象，可以对其进行read,readline,write等操作
# zipfile.setpassword(psw)，为zip文件设置默认密码
# zipfile.testzip() # 读取zip中的所有文件，验证他们的CRC校验和。返回第一个损坏文件的名称，如果所有文件都是完整的就返回None
# zipfile.write(filename[,arcname[,compression_type]]) # 将zip外的文件filename写入到名为arcname的子文件中（当然arcname也是带有相对zip包的路径的），打开方式为w或a
# zipfile.extract(member, path=None, pwd=None) # 解压一个zip中的文件，path为解压存储路径，pwd为密码
# zipfile.extractall(path[,pwd]) # 解压zip中的所有文件，path为解压存储路径，pwd为密码
while True:
    r = zipfile.is_zipfile(zip_src)  #是否是zip文件
    if r:
        fz = zipfile.ZipFile(zip_src,"r")   #读取zip中压缩文件

        fz.extractall(path="zip解压/",pwd=bytes(fz.filename.replace('.zip','').replace('zip解压/',""),encoding='utf-8'))   #解压,密码是[]

        zip_src="zip解压/"+fz.filelist[0].filename
    else:
        break