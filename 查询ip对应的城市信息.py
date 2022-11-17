
import scapy
from scapy.all import *
from scapy.utils  import  PcapReader
from pyecharts import *
def counts(array) :
  set1 =set(array)
  dict={}
  for item in set1:
      dict.update({item: array.count(item)})
  return dict
def pcapng(file_pcapng) :
  protocol = []
  time = []
  length=[]
  packets=rdpcap(file_pcapng)
  for data in packets:
    if 'IP' in data:
          length. append(data[IP].len)
    time.append(TimeStampToTime(data.time))
    protocol. append(data.payload.name)
  Barfile(counts(time), "时间直方图", "个数", "time.html")
  Barfile(counts(length), "长度直方图","单位是字节", "length.html")
  return protocol
def TimeStampToTime(timestamp) :
  timeStruct  = time.localtime(timestamp)
  return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)


def Barfile(list,title, sidenote, filename) :
  Bar_name_list=[]
  Bar_size_list=[]
  for key in list:
    Bar_name_list.append(key)
    Bar_size_list.append(list[key])
  bar=Bar(title,"")
  bar.add(sidenote,Bar_name_list, Bar_size_list)
  bar. show_config()
  bar.render( filename)
def main():
  file_pcapng="22.pcapng"
  pro=[]
  list=counts(pcapng(file_pcapng) )
  Barfile(list, "协议直方图", "协议个数","pro.html")
if __name__ =="__main__":
  main()





