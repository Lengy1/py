from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time


sl = {
    '体育分项':'/html/body/div[1]/div/div/div[4]/ul/li[3]/a',
    '主修课程':'/html/body/div[1]/div/div/div[4]/ul/li[1]/a',
    '通识选修课':'/html/body/div[1]/div/div/div[4]/ul/li[2]/a',
    '特殊课程':'/html/body/div[1]/div/div/div[4]/ul/li[4]/a',

    #一:填写登录学号与密码
    '学号':'20113316',
    '密码':'wmx15990697273'
}
week={
    '周一':'/html/body/div[1]/div/div/div[2]/div/div[3]/div[9]/div/div/ul/li[1]/a',
    '周二':'/html/body/div[1]/div/div/div[2]/div/div[3]/div[9]/div/div/ul/li[2]/a',
    '周三':'/html/body/div[1]/div/div/div[2]/div/div[3]/div[9]/div/div/ul/li[3]/a',
    '周四':'/html/body/div[1]/div/div/div[2]/div/div[3]/div[9]/div/div/ul/li[4]/a',
    '周五':'/html/body/div[1]/div/div/div[2]/div/div[3]/div[9]/div/div/ul/li[5]/a',
}
ls = [
    None,
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[1]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[2]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[3]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[4]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[5]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[6]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[7]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[8]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[9]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[10]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[11]/a',
    '/html/body/div[1]/div/div/div[2]/div/div[3]/div[10]/div/div/ul/li[12]/a'
]

#二:以下五项为要选课程的定位信息
CourseName = '散打'
nameofteacher = '吕亚崙'
module = '体育分项'
date = "周二"
#第几节
num = 1

browser_option = Options()
browser_option.add_argument('--disable-gpu')
browser_option.add_argument('blink-settings=imagesEnabled=true')

#三:填写chromedriver的路径
browser = webdriver.Chrome(
    executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe',
    options=browser_option)

#访问选课网站
browser.get('http://newjw.hdu.edu.cn/jwglxt/xtgl/index_initMenu.html')
time.sleep(2)

#登录行为

browser.find_element_by_name('yhm').send_keys(sl.get('学号'))
browser.find_element_by_id("mm").send_keys(sl.get('密码'))
browser.find_element_by_id("dl").click()

time.sleep(2)
#四:填写选课页面的URL及参数
browser.get('http://newjw.hdu.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=21042124')

while True:
    time.sleep(2)
    #选择周几
    browser.find_element_by_xpath(week.get(date)).click()
    #选择第几节
    browser.find_element_by_xpath(ls[num]).click()
    #这是定位到选课搜索栏
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/input').send_keys(CourseName)
    #选择模块，每个模块的xpath路径请看最下方代码
    browser.find_element_by_xpath(sl.get(module)).click()
    time.sleep(2)

    lessions = browser.find_elements_by_class_name("body_tr")
    target = None
    for lession in lessions:
        teacherName = lession.find_element_by_class_name("jsxmzc")
        if nameofteacher in str(teacherName.text):
            print('找到了'+nameofteacher)
            target = lession
    button = target.find_element_by_class_name("an")

    if button.text == '选课':
        button.click()
        print('点击中')
    else:
        print('选上了')
        break

    time.sleep(1)
    browser.refresh()
    browser.refresh()
    browser.refresh()

